from flask import Flask, render_template, request
app = Flask(__name__)

def callviews():
    from vicks import crud
    obj1 = crud.vicks(link = 'https://page-84a20-default-rtdb.firebaseio.com/')
    pageviews = obj1.pull(child = 'Views')
    pageviews += 1
    obj1.push(data = pageviews, child = 'Views')
    return pageviews

@app.route('/')
def index():
    name = 'Vicky Kumar'
    counter = callviews()
    return render_template('index.html',
                           name = name,
                           counter = counter,
                           )

@app.route('/about')
def about():
    skill = 'berogzar'
    return render_template('about.html', skill = skill)

@app.route('/video')
def video():
    return render_template('video.html', vid = 'feaf31ojyjq')

@app.route('/videopost', methods=['POST'])
def videopost():
    vid = request.form['vid']
    from vicks import crud
    obj1 = crud.vicks(link='https://page-84a20-default-rtdb.firebaseio.com/')
    obj1.push(data=vid, child='Video')
    return render_template('video.html', vid=vid)

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)