# pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/map')
def map():
    return render_template("")

def main():
    app.run(debug=True, port=80)

if __name__ == "__main__":
    main()