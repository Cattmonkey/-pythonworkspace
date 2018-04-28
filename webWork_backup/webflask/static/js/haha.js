//send message
function Postmessage(){
    var name=document.getElementById("UN").value;
    var message=document.getElementById("CM").value;
    var UserM='name=' + name + "&" + 'message=' + message;
    var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  } 
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    { //x=xmlhttp.responseXML.documentElement.getElementsByTagName("CD");
    }
  }
xmlhttp.open("post","/myblog_data",true);
xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;");  //用POST的
xmlhttp.send(UserM);//"username=abc&password=123"
alert(UserM);
}
