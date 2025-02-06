import json
from pathlib import Path
import pandas as pd


def main():
    language = 'it'
    base_path: Path = Path('.', 'crawled', language).resolve()
    save_path: Path = Path('.', 'annotation', language).resolve()
    max_sentences: int = 300

    df_data = {}
    for article in base_path.glob('*.json'):
        with article.open('r') as f:
            article_data = json.load(f)

        df_data.setdefault('sentence', []).extend(article_data['sentences'])
        df_data.setdefault('article_id', []).extend([article_data['title']] * len(article_data['sentences']))

    df = pd.DataFrame.from_dict(df_data)
    if len(df) > max_sentences:
        print(f'Dataset size is {len(df)}. Sampling up to {max_sentences}.')
        df = df.sample(n=max_sentences)

    # shuffle
    df = df.sample(frac=1.0)
    print(f'Storing dataset of size (no. sentences): {len(df)}/{max_sentences}')

    if not save_path.is_dir():
        save_path.mkdir(exist_ok=True, parents=True)

    df['label'] = None
    df.to_csv(save_path.joinpath('dataset.csv'), index=False)


if __name__ == '__main__':
    main()
