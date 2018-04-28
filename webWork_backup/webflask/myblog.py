#-*- coding: utf-8 -*-

#==============================================================================
# # -*- coding: utf-8 -*-
# from flask import  Flask
# from flask import render_template
#
# app = Flask(__name__,static_url_path='')
#
# #@app.route("/")
# #@app.route("/hello/<name>")
# #def helloWorld(name):
#     #return name
# @app.route("/")
# @app.route("/index")
# def index():
#     return render_template('html/index.html')
#
# #if __name__  == '__name__':
# app.debug = True
# #enter
# app.run(host='0.0.0.0',port=8080)
#==============================================================================
from flask import Flask
from flask import request, render_template, send_file
from werkzeug.routing import BaseConverter
#from model.datatest import datasql


class RegexConverter(BaseConverter):

    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter


@app.route("/<regex('[^\s]*'):name>")
def myblog(name):
    #sql = datasql()
    # sql.conn("test.db")
    if "" == name:
        htm = "index.htm"
        return send_file('templates/' + htm)
    namelist = name.split('.')
    if len(namelist) > 1:
        print(request.values)
        print(name)
        htm = name
        return send_file('templates/' + name)

    return name


@app.route("/myblog_data", methods=['GET', 'POST'])
def myblog_data():
    print(request.form)
    if request.method == 'POST':
        print(request.values.get("name"))

    return "yy"

if __name__ == '__main__':
    app.debug = True

    app.run(host='0.0.0.0', port=80, threaded = True)
    print("finish")
