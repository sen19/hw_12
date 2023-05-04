from flask import Blueprint, request, render_template
import logging
from main.utils import *
from config import POST_PATH
from exceptions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='test.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    logging.info("Открытие главной страницы")
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    s = request.args.get('s')
    logging.info(f"Поиск поста по слову: {s}")
    try:
        # Загрузка постов в переменную
        posts = load_posts(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"

    # функция поиска постов по слову
    filtered_posts = search_posts_by_substring(posts, s)
    return render_template('post_list.html', posts=filtered_posts, s=s)
