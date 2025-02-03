import json
from pathlib import Path
from typing import List, AnyStr

from newsplease import NewsPlease


def main():
    urls: List[AnyStr] = ...
    save_path: Path = Path('.', 'crawled').resolve()

    if not save_path.is_dir():
        save_path.mkdir(parents=True, exist_ok=True)

    articles = NewsPlease.from_urls(urls, timeout=30)
    for article_idx, url in enumerate(urls):
        article = articles[url]
        with save_path.joinpath(f'{article_idx}.json').open('w') as f:
            json.dump(article.get_serializable_dict(), f)


if __name__ == '__main__':
    main()
