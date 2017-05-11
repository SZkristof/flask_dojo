from flask import Flask, render_template

app = Flask(__name__)


@app.route('/request_counter', methods="GET")
def get_request_counter():
    
    return render_template("request_counter.html")


@app.route('/request_counter', methods="POST")
def post_request_coutner():
    return render_template("request_counter.html")

