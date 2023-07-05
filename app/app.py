from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('categories.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)