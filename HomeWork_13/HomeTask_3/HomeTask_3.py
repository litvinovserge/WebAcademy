"""
Изменить код «Доски объявлений»:
1. Чтобы у каждого объявления отображалась дата.
2. Добавить поля для ввода email при создании объявления. Отображать эмейл автора в объявлении.
3. Добавить поле для поиска объявлений. (Поиск просто по вхождению подстроки в текст объявления)
"""
from flask import Flask, redirect, render_template, request, url_for
import datetime

app = Flask(__name__)

posts = [
    {'name': 'Илья', 'email': 'ilya@mail.com', 'text': 'Продам гараж! 500грн. Звоните 0500351357', 'date': '2018-7-11'},
    {'name': 'Дмитрий', 'email': 'dima@mail.com', 'text': 'Потерял телефон. Iphone 6s 0662434658', 'date': '2018-7-12'},
    {'name': 'Даша', 'email': 'daria@mail.com', 'text': 'Куплю гараж!', 'date': '2018-7-13'},
]


@app.route('/')
def post_list():
    return render_template('post_list.html', posts=posts)


@app.route('/new_post/', methods=['GET', 'POST'])
def new_post():
    dt = datetime.datetime.now()
    post_date = f'{dt.year}-{dt.month}-{dt.day}'
    if request.method == 'GET':
        return render_template('new_post.html')
    elif request.method == 'POST':
        posts.append({
            'name': request.form['name'], 'text': request.form['text'], 'date': post_date, 'email': request.form['email']
        })
        return redirect(url_for('post_list'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
