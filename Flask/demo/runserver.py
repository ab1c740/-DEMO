__author__ = 'dev11'
from demo import app

@app.route('/')
def hello_world():
    return  '<h1>Hello World!</h1>'

if __name__=="__main__":
    app.run(debug=True)