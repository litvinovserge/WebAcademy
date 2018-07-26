"""
1. Создать сайт "Генератор случайных чисел" c одним окном где отображено случайное число и кнопка "сгенерировать" новое
число.
2. Добавить возможность задания диапазона в котором генерируются случайные числа.
"""
from flask import Flask, redirect, render_template, request, url_for
import random

DEFAULT_LIMITS = [-10000, 10000]
TEMP_FILE = 'tmp.txt'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generated_number', methods=['GET', 'POST'])
def generator():
    if request.method == "POST":
        if all((request.form['min_gen_number'].isdigit(), request.form['max_gen_number'].isdigit())):
            limits = [int(request.form['min_gen_number']), int(request.form['max_gen_number'])]
            with open(TEMP_FILE, 'w') as file:
                file.write(str(limits))
        else:
            limits = DEFAULT_LIMITS
            with open(TEMP_FILE, 'w') as file:
                file.write(str(limits))

    with open(TEMP_FILE, 'r') as file:
        limits = file.read()
    limits = limits.replace('[', '')
    limits = limits.replace(']', '')
    limits = limits.split(',')

    return render_template('generated.html', random_number=random.randint(int(limits[0]), int(limits[1])))


if __name__ == "__main__":
    app.run(debug=True,  port=int("8080"))