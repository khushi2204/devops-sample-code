from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "HyperServe Flask OK"

if __name__ == '__main__':
    # default Flask port inside container: 5000
    app.run(host='0.0.0.0', port=5000)
