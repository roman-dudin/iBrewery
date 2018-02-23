from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
recipes = []
app.config['SECRET_KEY'] = 'dsfsdf'


def store_recipe(recipe_name):
    recipes.append(dict(
        recipe_name=recipe_name,
        user='username',
        date=datetime.utcnow()
    ))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        store_recipe(recipe_name)
        flash('Stored recipe "{}"'.format(recipe_name))
        return redirect(url_for('index'))
    return render_template('add_recipe.html')


if __name__ == '__main__':
    app.run(debug=True)
