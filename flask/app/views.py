from app import app
from flask import request, jsonify, abort, json
from flask import make_response, session
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from werkzeug import secure_filename
from Blogmodel import *
from Blogcontroler import *
import os
import time
import base64

UPLOAD_FOLDER='../blog2017/static/images'
ALLOWED_EXTENSIONS = set(['txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
basedir = os.path.abspath(os.path.dirname(__file__))

User=user()
Articles=articles()
Comment=comment()

def authenticate(username, password):
    print('>>> n2 = %s' % username)
    JWT_EXPIRATION_DELTA=30000
    data=User.login(username,password)
    if(data.get('status')==200):
        return user_controler(data['id'],username,password,data['access'])

def identity(payload):
    user_id = payload['identity']
    access=User.getaccess(user_id)
    return {'id':user_id,'access':access}

app.config['SECRET_KEY'] = 'yuliang'
jwt = JWT(app, authenticate, identity)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/user/regist', methods = ['POST'])
def user_regist():
    name=request.form['username']
    password=request.form['password']
    github=request.form['github']
    wechat=request.form['wechat']
    info=request.form['info']
    create=request.form['create']
    access=0
    status=User.create(**{'name':name,'password':password,'github':github,'wechat':wechat,'info':info,'create':create,'access':0})
    return jsonify(status)


@app.route('/user/revise', methods = ['POST'])
@jwt_required()
def user_revise():
    password=request.form['password']
    github=request.form['github']
    wechat=request.form['wechat']
    info=request.form['info']
    id=current_identity['id']
    status=User.update(**{'password':password,'github':github,'wechat':wechat,'info':info,'id':id})
    return jsonify({'status':'success','code':status})

@app.route('/user/info', methods = ['GET'])
def user_info():
    id = request.args.get('name', '')
    data=User.getinfo(id)
    if str(data)=='None' :
        return jsonify({'status':'error','info':'no user found'})
    else :
        return jsonify({'status':'success','data':{'id':data[0],'username':data[1],'github':data[3],'wechat':data[4],'info':data[5]}})

@app.route('/user/delete', methods = ['GET'])
@jwt_required()
def user_delete():
    id = request.args.get('id', '')
    print(current_identity)
    if current_identity['access'] == 9:
        sta=User.delete(id)
        return jsonify({"status": "success","code":sta})
    else:
        return jsonify({"status":"error","info":"access denied"})

@app.route('/user/all', methods = ['GET'])
@jwt_required()
def user_getall():
    datas=User.serach_all();
    data=list()
    for i in datas:
        map={'id':i[0],'name':i[1],'github':i[3],'wechat':i[4],'info':i[5],'create':i[6]}
        data.append(map)
    return jsonify({'status':'success','data':data})


@app.route('/articles', methods = ['GET'])
def article_getall():
    id=str(request.args.get('class', ''))
    datas=Articles.serach_muti(id);
    data=list()
    for i in datas:
        map={'id':i[0],'img':i[1],'subtitle':i[2],'class':i[3],'author':i[4],'create':i[5],'update':i[6],'counts':i[7],'title':i[8],'content':i[9]}
        data.append(map)
    return jsonify({'status':'success','data':data})

@app.route('/articles/all', methods = ['GET'])
@jwt_required()
def article_all():
    datas=Articles.serach_all();
    data=list()
    for i in datas:
        map={'id':i[0],'img':i[1],'subtitle':i[2],'class':i[3],'author':i[4],'create':i[5],'update':i[6],'counts':i[7],'title':i[8],'content':i[9]}
        data.append(map)
    return jsonify({'status':'success','data':data})

@app.route('/article', methods = ['GET'])
def article_getone():
    id=request.args.get('id', '')
    i=Articles.search_one(id)
    print(i)
    if str(i) != 'None':
        map={'id':i[0],'img':i[1],'subtitle':i[2],'class':i[3],'author':i[4],'create':i[5],'update':i[6],'counts':i[7],'title':i[8],'content':i[9]}
        return jsonify({'status':'success','data':map})
    else :
        return jsonify({'status':'error','data':''})

@app.route('/article/delete', methods = ['POST'])
@jwt_required()
def article_delete():
    id=request.form['id']
    if current_identity == 9  :
        return jsonify({'status':'success','code':Articles.delete(id)})
    else :
        return jsonify({'status':'error','info':'access denied'})

@app.route('/article/create', methods = ['POST'])
@jwt_required()
def article_create():
    if current_identity['access'] == 9 or current_identity['access'] == 8 :
        status=Articles.create(**request.form)
        return jsonify({'status':'success','code':status})
    else :
        return jsonify({'status':'error','info':'access denied'})

@app.route('/article/revise', methods = ['POST'])
@jwt_required()
def article_revise():
    if current_identity['access'] == 9 or current_identity['access'] == 8 :
        status=Articles.update(**request.form)
        return jsonify({'status':'success','code':status})
    else :
        return jsonify({'status':'error','info':'access denied'})

@app.route('/article/count', methods = ['GET'])
def article_count():
    id=request.args.get('id', '')
    status=Articles.count(id)
    return jsonify({'status':'success','code':status})

@app.route('/comment/create', methods = ['POST'])
@jwt_required()
def comment_create():
    sta=Comment.create(**request.form)
    return jsonify({'status':'success','code':sta})

@app.route('/comment/son', methods = ['GET'])
def comment_search():
    datas=Comment.search_son(request.args.get('id', ''))
    cuple=list()
    for data in datas:
        map={"id":data[0],"content":data[1],"name":data[2],"create":data[3],"fatherid":data[4],"sonid":data[5],"for":data[6]}
        cuple.append(map)
    return jsonify({'status':'success','data':cuple})

@app.route('/comment/article',methods=['GET'])
def comment_one():
    datas=Comment.search_article(request.args.get('id', ''))
    cuple=list()
    for data in datas:
        map={"id":data[0],"content":data[1],"name":data[2],"create":data[3],"fatherid":data[4],"sonid":data[5],"for":data[6]}
        cuple.append(map)
    return jsonify({'status':'success','data':cuple})

@app.route('/comment/count', methods = ['GET'])
def comment_count():
    data=Comment.count(request.args.get('id', ''))
    return jsonify({'status':'success','code':data})

@app.route('/comment/delete', methods = ['GET'])
@jwt_required()
def comment_delete():
  if current_identity['access'] == 9 or current_identity['access'] == 8 :
       sta=Comment.delete(request.args.get('id',''))
       return jsonify({'status':'success','code':sta})
  else :
      return jsonify({'status':'error','info':'access denied'})

@app.route('/comment/all', methods = ['GET'])
@jwt_required()
def comment_getall():
    datas=Comment.serach_all();
    data=list()
    for i in datas:
        map={'id':i[0],'content':i[1],'name':i[2],'create':i[3],'fatherid':i[4],'sonid':i[5],'for':i[6]}
        data.append(map)
    return jsonify({'status':'success','data':data})

@app.route('/album/upload', methods = ['POST'])
def album_upload():
    file = request.files['img']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return jsonify({'status':'success','url':os.path.relpath(filename)})
@app.route('/album/create', methods = ['POST'])
def album_create():
  return 'onworking'

@app.route('/album/delete', methods = ['POST'])
def album_delete():
  return 'onworking'

@app.route('/album/revise', methods = ['POST'])
def album_revise():
  return 'onworking'

@app.route('/album/count', methods = ['POST'])
def album_count():
  return 'onworking'

@app.route('/album/imgs', methods = ['GET'])
def album_imgs():
  return 'onworking'

@app.route('/album/img', methods = ['GET'])
def album_img():
  return 'onworking'

@app.errorhandler(404)
def not_found(e):
  return make_response(jsonify({'error':'Not Found'}),404)
