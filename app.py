from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Vicky Kumar'
    return render_template('index.html', name = name)

@app.route('/about')
def about():
    skill = 'berogzar'
    return render_template('about.html', skill = skill)

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)