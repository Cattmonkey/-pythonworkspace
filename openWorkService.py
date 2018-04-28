# coding=UTF-8
from datetime import datetime
import glob
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify, Response
import requests
import matplotlib.image as mpimg  # mpimg 用于读取图片
from flask_cors import CORS
# from model.heatmapAPINew import getHeat

from auto_tool.autoHtml import AutoHtml
# from PIL import Image

app = Flask(__name__)
# 跨域
CORS(app)

app.config['DEBUG'] = True

arg = "id"

# localUrl = "192.168.100.249"

localIp = "localhost"  # "192.168.104.80"
serverPort = 80
localUrl = "http://" + localIp + ":" + str(serverPort) + "/pml_model"
# dockerUrl = "http://192.168.100.249:9090/"  # "http://192.168.100.248:19090/"

autohtmlPath = "templates/"  # "auto_tool/"
autohtml = "test.html"
pmlPath = "preRead.pml"


@app.route('/pml_model')
@app.route('/pml_model', methods=['POST', 'GET'])
def pml_model():
    print("update test.html by preRead.pml")

    AutoHtml(pmlPath).createHtml(localUrl, autohtmlPath + autohtml)
    print('method', request.method)
    if request.method == 'POST':
        print(request.headers)
        print(request.form)

# if len(sys.argv) < 2:
#     transformer = PmlTransformer()
#     #expr_asts, funName = transformer.runPmlTransformer()
#     for funName_expr_ast in transformer.runPmlTransformer():
#         #    print(iexpr_ast
#         for funName, expr_ast in funName_expr_ast.items():
#             eval(compile(expr_ast, '<test' + funName + '>' , 'exec'))
#             print("def", funName)
#             print(eval(funName + "('yyx')"))
# else:
#     if "pml_" in sys.argv[1]:
#         transformer = PmlTransformer()
#         for funName_expr_ast in transformer.runPmlTransformer():
#             for funName, expr_ast in funName_expr_ast.items():
#                 eval(compile(expr_ast, '<test' + funName + '>' , 'exec'))
#                 print("def", funName)
#         print("do", sys.argv[1].split("_")[1])
#         print('result:', eval(sys.argv[1].split("_")[1] + "('" + sys.argv[2] + "')"))
                 
#     if sys.argv[1] == "phModel":
#         print(odp.tel_model_juhe(sys.argv[2]))
#     if sys.argv[1] == "heatmap":
#         print(odp.heatmap())

    return render_template(autohtml)


# print("hello")
print("自动生成html")
AutoHtml(pmlPath).createHtml(localUrl, autohtmlPath + autohtml)
app.run(host=localIp, port=serverPort, threaded=True)

# app.run(host='0.0.0.0', port=8088)
# dataSupport = DataSupport()
# print(dataSupport.pcmModel('http://192.168.100.249:9090/', 'phModel', '15801079068'))
