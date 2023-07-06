from flask import (Flask, render_template, request,
                   redirect, flash, url_for)
from db.categories import Category

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/categories/')
def categories():
    categories = Category.get_all()
    return render_template('categories.html',
                           categories=categories)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

@app.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        if not category:
            flash('Debes ingresar una Categoría')
        elif not description:
            flash('Debes ingresar una descripcion')
        else:    
            cat = Category(category, description)
            cat.save()
            return redirect(url_for('categories'))
    return render_template('create_cat.html')

@app.route('/categories/<int:id>/update/')
def update_cat(id):
    #Obtener Cat desde id
    #Enviar datos a form
    return "Lo vamos a Actualizar"

@app.route('/categories/<int:id>/delete/')
def delete_cat(id):
    #Obtener Cat desde id
    cat = Category.get(id)
    cat.delete()
    #Enviar datos a form
    return redirect(url_for('categories'))

if __name__ == '__main__':
    app.run(debug=True)