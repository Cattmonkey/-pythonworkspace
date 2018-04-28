# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/")
def getbook():
    return render_template('index.htm')

if __name__  == '__main__':
    app.debug = True
    
    app.run(host='0.0.0.0',port=80)
    print("finish")