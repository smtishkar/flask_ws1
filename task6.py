# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах. 
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", 
# "Средний балл". Данные о студентах должны быть переданы в шаблон через контекст.


from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/')
def index():
    context= [
        {'name': 'Ivan',
         'lastname': 'Ivanov',
         'age': 24},
        {'name': 'Petr',
         'lastname': 'Sidorov',
         'age': 34},
        {'name': 'Dmitry',
         'lastname': 'Kolosov',
         'age': 44}
    ]

    return render_template('task6.html.', context=context)

if __name__ == '__main__':
    app.run(debug=True)