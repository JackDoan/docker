from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def bopis():
    return "<h1>Buy online, pick up in store!</h1>"
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
