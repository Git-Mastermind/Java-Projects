from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')

def hello():
    return print('Hello World')

if __name__ == '__main__':
    app.run(debug=True)