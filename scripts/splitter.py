from wtpsplit import SaT
import json
from pathlib import Path
from tqdm import tqdm
import string


def load_text(text_path: Path):
    with text_path.open('r') as f:
        article_data = json.load(f)

    return article_data['text'], article_data


def parse_sentences(sentences):
    MIN_SIZE = 5

    aggregated = 0
    parsed = []
    for sent in sentences:
        mod_sent = sent.translate(str.maketrans('', '', string.punctuation))

        # aggregate to previous (no loss of data)
        if len(mod_sent) < MIN_SIZE and len(parsed):
            parsed[-1] += f' {mod_sent}'
            aggregated += 1
        else:
            parsed.append(sent)

    return parsed, aggregated


def main():
    model = 'sat-6l-sm'
    language = 'it'
    base_path = Path('.', 'crawled', language).resolve()

    sat = SaT(model, language=language, style_or_domain='ud')
    sat.half().to('cuda')

    text_paths = list(base_path.glob('*.json'))
    total_aggregated = 0
    total_sentences = 0
    for text_path in tqdm(text_paths, desc='Splitting crawled articles...'):
        text, article_data = load_text(text_path=text_path)

        if article_data is None:
            continue

        sentences, aggregated = parse_sentences(sat.split(text))
        total_sentences += len(sentences)
        total_aggregated += aggregated
        article_data['sentences'] = sentences

        with text_path.open('w') as f:
            json.dump(article_data, f, indent=4)

    print(f'Sentences: {total_sentences}. Aggregated: {total_aggregated}')


if __name__ == '__main__':
    main()
