from wtpsplit import SaT
import json
from pathlib import Path
from tqdm import tqdm


def load_text(text_path: Path):
    with text_path.open('r') as f:
        article_data = json.load(f)

    return article_data['text'], article_data


def main():
    model = 'sat-6l-sm'
    language = 'pl'
    base_path = Path('.', 'crawled', language).resolve()

    sat = SaT(model, language=language, style_or_domain='ud')
    sat.half().to('cuda')

    text_paths = list(base_path.glob('*.json'))
    for text_path in tqdm(text_paths, desc='Splitting crawled articles...'):
        text, article_data = load_text(text_path=text_path)

        if article_data is None:
            continue

        sentences = [sent for sent in sat.split(text) if len(sent.strip())]
        article_data['sentences'] = sentences

        with text_path.open('w') as f:
            json.dump(article_data, f, indent=4)


if __name__ == '__main__':
    main()
