import json
from pathlib import Path

import trafilatura
from newsplease import NewsPlease
import newspaper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urls import get_english_urls
from tqdm import tqdm
import time


def scroll_down(driver):
    """
    Scrolls down the page to load all content.
    Taken from: https://github.com/adbar/trafilatura/issues/85
    """

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def trafilatura_crawler(url):
    """
    Main crawler using selenium to avoid popup and blockers.
    """
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    scroll_down(driver=driver)

    downloaded = trafilatura.load_html(driver.page_source)
    text = trafilatura.extract(downloaded)
    metadata = trafilatura.extract_metadata(downloaded)

    driver.quit()

    if text is None:
        return None

    return {
        'url': url,
        'language': metadata.language,
        'title': metadata.title,
        'text': text
    }


def newsplease_crawler(url):
    """
    Retro-compatibility backup crawler.
    """
    article = NewsPlease.from_url(url, timeout=30)

    if article.text is None and article.maintext is None:
        return None

    return {
        'url': url,
        'language': article.language,
        'title': article.title,
        'text': article.text if article.maintext is None else article.maintext
    }


def newspaper4k_crawler(url, language):
    """
    Retro-compatibility backup crawler.
    """
    article = newspaper.article(url=url, language=language)

    if article.text is None:
        return None

    return {
        'url': url,
        'language': language,
        'title': article.title,
        'text': article.text
    }


def save_article_content(save_path, article_content, article_idx):
    with save_path.joinpath(f'{article_idx}.json').open('w') as f:
        json.dump(article_content, f, indent=4)


def main():
    urls, language = get_english_urls()
    save_path: Path = Path('.', 'crawled', language).resolve()

    if not save_path.is_dir():
        save_path.mkdir(parents=True, exist_ok=True)

    for article_idx, url in tqdm(enumerate(urls), desc='Crawling articles...', total=len(urls)):
        article_content = trafilatura_crawler(url=url)
        if article_content is not None:
            save_article_content(save_path=save_path, article_content=article_content, article_idx=article_idx)
            continue

        article_content = newsplease_crawler(url=url)
        if article_content is not None:
            save_article_content(save_path=save_path, article_content=article_content, article_idx=article_idx)
            continue

        article_content = newspaper4k_crawler(url=url, language=language)
        if article_content is not None:
            save_article_content(save_path=save_path, article_content=article_content, article_idx=article_idx)
            continue

        print(f'Could not retrieve article {article_idx} content! Skipping...')


if __name__ == '__main__':
    main()
