from flask import Blueprint, request, render_template
import logging
from main import utils
from loader.utils import *
from config import POST_PATH

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='test.log', level=logging.INFO)


@loader_blueprint.route('/post', methods=['GET'])
def add_new_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_new_post_by_user():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных")
        return "Отсутствует часть данных"

    # загрузка постов в переменную
    posts = utils.load_posts(POST_PATH)
    try:
        new_post = {'pic': save_picture(picture), 'content': content}
    except WrongImgType:
        return "Неверный формат файла! Допустимы только jpg, png, gif, jpeg"

    # Функция добавления нового поста
    add_post(posts, new_post)
    return render_template('post_uploaded.html', new_post=new_post)
