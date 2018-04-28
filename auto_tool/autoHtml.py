# -*- coding: utf-8 -*-

from auto_tool.pyh import *


class AutoHtml:
    

    def __init__(self, pmlPath = "preRead.pml"):
        self.pmlPath = pmlPath

    def readPml(self, path):
        #读取pml文件进行语法
        with open(path) as f:
            for i in f.read().strip().replace("\n", "").split(","):
                yield dict([j.split(":") for j in i.split(";") if j != ""])
        pass




# =============================================================================
# funName:phModel;
# import_module:model.testMode;
# callmain:main;
# ,
# funName:phModel1;
# import_module:model.testMode1;
# callmain:main1;
# =============================================================================

    def createHtml(self, url = "http://192.168.100.249:8088/pml_model", 
                   htmlPath = "test.html"):
        
        page = PyH('AutoHtml')
        page.addCSS('static/css/bootstrap.min.css', 
                    'http://ictclas.nlpir.org:80/nlpir/css/index.css')
        page.addJS('static/js/jquery-1.7.2.js', 
                   'static/js/jquery.min.js', 
                   'static/js/bootstrap.min.js', 
                   'static/js/spin.js', 
                   'static/js/layer_mobile/layer.js')
        page << h1('autoHtml', cl='center', style="color:red;")
        page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p(u'自动生成界面', style="color:#66b3ff", id='myP1')
        mydiv2 = page << div(id='myDiv2')
        mydiv2 << h2(u'已加载模型导航', style="color:red;") + p(u'下面是通过pml加载的模型', style="color:#66b3ff")
        #设置导航
        page << div(id='modelList')
        page.modelList.attributes['cl'] = 'modelList'
        page.modelList.attributes['style'] = 'margin-top: 10px;list-style:none;'
        page.modelList << div(cl = "row", style=
                              "position:relative;background:#dddee2;padding-bottom:1%;"
                                  ) << div(
                                          cl = 'col-md-12 center-block'
                                  ) << ul(cl = "nav nav-pills", 
                                          style="margin-left:4%;font-size: 16px;color: #000;line-height: 34px;"
                                  ) 
        
        for i in self.readPml(self.pmlPath):
            
            print(page.modelList.div.div.ul << li(
                    role="presentation") << a(i['funName'], 
                    id = i['funName'], type = "button", 
                    onclick="chooseModel('" + i['funName'] + "')", target="_black"))
            print(i)
        
        page << div(id="form")
        page.form << h1('', id = 'chooseModel', style="color:red;")
        #page.form << br()
        page.form << h1(u'请求与返回结果', cl='form', style="color:red;")
        page.form << div(id="img_wait", style="display:none;")
        page.form << input(id = "phone")
        page.form << input(id = "submit", type = "submit")
        page.form << br()
        page.form << h2(u'返回结果', style="color:#66b3ff")
        page.form << br()
        page.form << textarea(id = "output" ,cl = 'form-control', rows="6")
        
        # =============================================================================
        # <textarea rows="3" cols="20">
        # 
        # </textarea>
        # =============================================================================
        
        
        #添加js代码
        page << script(
        '''
        var opts = {
         lines: 9,
         length: 0,
         width: 15,
         radius: 20,
         corners: 1,
         rotate: 0,
         direction: 1,
         color: '#0101DF',
         speed: 1, 
         trail: 34,
         shadow: false,
         hwaccel: false,
         className: "spinner",
         zIndex: 2e9,
         top: '50',
         left: '50'
        };
        
        var target = document.getElementById('img_wait');
        var spinner = new Spinner(opts).spin(target);
        var modelName = "";
        
               function chooseModel(name){
                   modelName = name
                   if (name == 'submit'){
                     console.log(name)
                   }else{
                       console.log(name)
                       //document.getElementById("input").value  = ""
                       //document.getElementById("input").value 
                       //      = document.getElementById(name).text
                       
                       document.getElementById("chooseModel").innerHTML  = name
                   }
               }
                   
              $(function() {
        		    $('#submit').click(function() {
        		      var userPhone = $('#phone').val().trim(); //联系方式
                  if(userPhone == ''){
                    //提示
                      layer.open({
                      content: '手机号不能为空!'
                      ,skin: 'msg'
                      ,time: 2 //2秒后自动关闭
                      });
                    return false;
                  };
        
                  //联系方式正则表达式
                  var isPhone = /(1[3-9]\d{9}$)/;
                  var isMob = /^0\d{2,3}-?\d{7,8}$/;
                  if(isMob.test(userPhone) || isPhone.test(userPhone)){
                      console.log(userPhone);
                  }
                  else{
                      layer.open({
                      content: '请输入正确的手机号!'
                      ,skin: 'msg'
                      ,time: 2 //2秒后自动关闭
                      });
                  }
                if(modelName == ""){
                      console.log("模型:" + modelName);
                      //提示
                      layer.open({
                      content: '请先选择模型!'
                      ,skin: 'msg'
                      ,time: 2 //2秒后自动关闭
                      });
                    return false
                  };

              //setData("")//清空数据
              //等待效果
              document.getElementById('img_wait').style.display='block';
              //Ajax提交
                $.ajax({
                  url: '%s',
                  type: "post",
                  dataType: "json",
                  data:{
                    //"company": company, 
                    //"contacts": contacts, 
                    "phone": userPhone,
                    "funName": modelName,
                    //"source": "pc", 
                    //"entryName": "solicitation"
                  },
                  success:function (data){
                      //alert(data)
                      //glData = JSON.stringify(data, undefined, 4)
                      //document.getElementById('img_wait').style.display='block';
                      //var t=setTimeout("setData(glData);",2000)//故意
                      //setData(glData);
                      //setData(data);
                      document.getElementById('img_wait').style.display='none';
                      var element=document.getElementById("output");
                      element.innerHTML = data;
                      
                      layer.open({
                      content: '提交成功！'
                      ,skin: 'msg'
                      ,time: 2 //2秒后自动关闭
                      });
                        
                  },
                  error: function () {
                     //提示
                     //display:none
                     //停止等待效果
                      document.getElementById('img_wait').style.display='none';
                      layer.open({
                      content: '提交失败！'
                      ,skin: 'msg'
                      ,time: 2 //2秒后自动关闭
                      });
                   }
                })
        
        		})
            })
        '''  % (url)
             )
        
        html = page.printOut(htmlPath)

#AutoHtml().createHtml()





