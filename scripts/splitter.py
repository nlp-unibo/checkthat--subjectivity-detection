from wtpsplit import SaT
import json
from pathlib import Path
from tqdm import tqdm


def load_text(text_path: Path):
    with text_path.open('r') as f:
        article_data = json.load(f)

    if 'sat_split' in article_data:
        return None, None

    if article_data['text'] is not None:
        return article_data['text'], article_data

    return article_data['maintext'], article_data


def main():
    model = 'sat-3l-sm'
    base_path = Path('.', 'crawled').resolve()

    sat = SaT(model, language='el', style_or_domain='ud')
    sat.half().to('cuda')

    text_paths = list(base_path.glob('*.json'))
    for text_path in tqdm(text_paths, desc='Splitting crawled articles...'):
        text, article_data = load_text(text_path=text_path)

        if article_data is None:
            continue

        sentences = [sent for sent in sat.split(text) if len(sent.strip())]
        article_data['sat_split'] = sentences

        with text_path.open('w') as f:
            json.dump(article_data, f)


if __name__ == '__main__':
    main()
