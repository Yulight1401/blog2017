## 将该博客部署到服务器的正确姿势：

### 1.服务器安装python模块 ： 

`pip install flask,flask-jwt,mysql-connector,pymsql,`

创建数据库：

`cd flask`

`python createDB.py`

启用flask

`python run.py`

### 2.本地打造Production版本

`cd blog2017`

`npm install`

`npm run build`

在./dist 得到 static目录 和 index.html

将dist下的所有文件，放到你提供网页服务的根目录里

flask目录和dist目录在同一层级

这样博客就正常运作了

### Blog 2017 数据库与接口设计

database:blog2017 tables:user,articles,comment,album

需求 1：用户登录，对接口有token验证系统

![](http://img.blog.csdn.net/20160723154518396?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

1.将荷载payload，以及Header信息进行Base64加密，形成密文payload密文，header密文。


2.将形成的密文用句号链接起来，用服务端秘钥进行HS256加密，生成签名.


3.将前面的两个密文后面用句号链接签名形成最终的token返回给服务端

注：

（1）用户请求时携带此token（分为三部分，header密文，payload密文，签名）到服务端，服务端解析第一部分（header密文），用Base64解密，可以知道用了什么算法进行签名，此处解析发现是HS256。

（2）服务端使用原来的秘钥与密文(header密文+"."+payload密文)同样进行HS256运算，然后用生成的签名与token携带的签名进行对比，若一致说明token合法，不一致说明原文被修改。

 （3）判断是否过期，客户端通过用Base64解密第二部分（payload密文），可以知道荷载中授权时间，以及有效期。通过这个与当前时间对比发现token是否过期。

三，实现思路

![](http://img.blog.csdn.net/20160723193343759?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

1.用户登录校验，校验成功后就返回Token给客户端。

2.客户端收到数据后保存在客户端

3.客户端每次访问API是携带Token到服务器端。

4.服务器端采用filter过滤器校验。校验成功则返回请求数据，校验失败则返回错误码

用户表：user: _name,_password,_github,_wechat,_info,_access(和自己一起作为博客管理者,0为普通用户，520为协作用户，999为管理员)

api:post /user/login? name&password return settoken,status 

api:post /user/regist? name&password&github return status settoken

api:post /user/revise? 上述所有参数 (带token)

get /user_info name return users info (with token)

需求二：博客系统

表设计：articles: _title,_img,_subtitle,_class,_author,_content,_create,_update(datetime),_counts

api:
get /get_articles?classnum return articles of one class

get /get_article?articleid return one 

post /delete_article articleid return status (with token)

post /create_article 上述所有参数 return status (with token)

post /revise_article 上述所有参数 return status (with token)

post /count_article aritcleid  return status
   

需求三：评论与字评论系统

表设计:comment: _name,_content,_create,_fatherid,_sonid(有儿子?儿子id:-1),_for 利用链表的结构

api:get /comment/all?fatherid return all son comments {num: ,comments:[{}]}  根据文章id返回关于该文章的所有评论


api:get /comment/one?id return all son comments {num: ,comments:[{}]}  id返回评论

api:post /comment/create 上述所有参数 回复时，同时设置父评论的子评论id，后台创建成功后，搜索父评论并设置其自评论 return status

需求四：相册系统

表设计：album: img,content，create,update,counts,author,class

api: xhr /album/upload 上传图片并且收集到/img目录下

get /get_imgs 获取img目录下，所有图片的路径
     
post /create_album 上述所有参数 return status

post /delete_album albumid return status 

post /count_article aritcleid  return status

get /get_albums classid return imgs in a class

get /get_album  return a img  

需求五：音乐系统

表：music:


##设计需求 
主色调:白色 ，辅助：黑，灰


重要改动：

comment sonid ->用于储存评论对应的文章id，查找文章的评论的时候，先取得所有关于文章的评论
通过fatherid，查找关于该评论的所有子评论

回复文章：设置sonid = 文章id ,fatherid=-1

回复评论：设置fatherid = 评论id ，sonid=-1

评论单独为组件，利用props传递数据
