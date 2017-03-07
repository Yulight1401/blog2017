/* eslint-disable */
function setCookie(c_name, value, expiredays){
　	var exdate=new Date();
　	exdate.setDate(exdate.getDate() + expiredays);
　	document.cookie=c_name+ "=" + escape(value) + ((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
}
function getCookie(c_name){
　　　　if (document.cookie.length>0){　　
　　　　　　let c_start=document.cookie.indexOf(c_name + "=")　　　　
　　　　　　if (c_start!=-1){
　　　　　　　　c_start=c_start + c_name.length+1　　
　　　　　　　　let c_end=document.cookie.indexOf(";",c_start)　　
　　　　　　　　if (c_end==-1) c_end=document.cookie.length　　
　　　　　　　　return unescape(document.cookie.substring(c_start,c_end))　　
　　　　　　}
　　　　}
　　　　return ""
}
function delCookie(c_name) {
  var exp = new Date();
  exp.setTime(exp.getTime() + (-1 * 24 * 60 * 60 * 1000));
  var cval = GetCookieValue(name);
  document.cookie = name + "=" + cval + "; expires=" + exp.toGMTString();
}
let Cookie={};
Cookie.set = setCookie
Cookie.delete = delCookie
Cookie.get = getCookie
export default Cookie;
