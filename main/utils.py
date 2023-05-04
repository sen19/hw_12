import json
from exceptions import *


def load_posts(path):
    """Функция загрузки постов"""

    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, substring):
    """Функция получения постов по слову"""

    post_founded = []
    for post in posts:
        if substring.lower() in post['content'].lower():
            post_founded.append(post)
    return post_founded
