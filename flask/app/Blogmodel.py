import pymysql
import sys

INSERTUSER = 'INSERT INTO user(_name, _password,_github,_wechat,_info,_create,_access) VALUES(%s, %s, %s, %s, %s, %s, %s)'
UPDATEUSER='UPDATE user SET _password=%s,_github=%s,_wechat=%s,_info=%s WHERE _id=%s'
SEARCHUSER = "SELECT * FROM user WHERE _name=%s"
DELETEUSER='DELETE FROM user WHERE _id=%s'
SEARCHUSERBYID='SELECT * FROM user WHERE _id=%s'
SEARCHALLUSER='SELECT * FROM user'

INSERTARTICLE='INSERT INTO articles(_img,_subtitle,_author,_create,_update,_title,_content,_class,_counts) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
SEARCHCLASSARTICLES='SELECT * FROM articles WHERE _class = %s '
SEARCHONEARTICLE='SELECT * FROM articles WHERE _id=%s '
UPDATEARTICLE='UPDATE articles SET _img=%s,_subtitle=%s, _author=%s,_update=%s,_title=%s, _content=%s, _class=%s WHERE _id=%s'
COUNTARTICLE='UPDATE articles SET _counts=_counts+1 WHERE _id=%s'
DELETEARTICLE='DELETE FROM ariticles WHERE _id=%s'
SEARCHALLARTICLE='SELECT * FROM articles'

INSERTCOMMENT='INSERT INTO comment(_name,_content,_create,_fatherid,_sonid,_for) VALUES(%s,%s,%s,%s,%s,%s)'
SEARCHSONCOMMENT='SELECT * FROM comment WHERE _fatherid=%s'
SEARCHONECOMMENT='SELECT * FROM comment WHERE _sonid=%s'
DELETECOMMENT='DELETE FROM comment WHERE _id=%s'
COUNTCOMMENT='UPDATE comment SET _for=_for+1 WHERE _id=%s'
SEARCHALLCOMMENT='SELECT * FROM comment'

reload(sys)
sys.setdefaultencoding("utf8")

def init_mysql():
    conn = pymysql.connect(host = "127.0.0.1", port = 3306, user = "root", password = "yuliang", db = "blog2017", charset = "utf8")
    return conn

class user():
    """docstring for ."""
    def create(self,**data):
        print(data)
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHUSER,data['name'])
        sta = cursor.fetchone()
        print(sta)
        print('status:'+str(sta=='None'))
        if str(sta)=='None':
            sta=cursor.execute(INSERTUSER,(data['name'],data['password'],data['github'],data['wechat'],data['info'],data['create'],0))
            print(sta)
            conn.commit()
            conn.close()
            return {'status':'success','code':sta}
        else:
            print(sta)
            conn.commit()
            conn.close()
            return {'status':'error','info':'invalid username'}


    def delete(self,id):
        conn = init_mysql()
        cursor = conn.cursor()
        sta = cursor.execute(DELETEUSER,(int(id)))
        conn.commit()
        conn.close()
        return sta;

    def login(self,name,password):
        conn = init_mysql()
        cursor = conn.cursor()
        print('>>> n3 = %s' % name)
        print('>>> n4 = %s' % password)
        cursor.execute(SEARCHUSER,name)
        data = cursor.fetchone()
        if str(data)=='None':
            conn.commit()
            conn.close()
            return {'status':404}
        else :
            if data[2] == password:
                conn.commit()
                conn.close()
                return {'status':200,'id':data[0],'access':data[6]}
            else :
                conn.commit()
                conn.close()
                return {'status':202}

    def update(self,**data):
        conn = init_mysql()
        cursor = conn.cursor()
        sta = cursor.execute(UPDATEUSER,
                            (data['password'],data['github'],data['wechat'],data['info'],data['id']))
        conn.commit()
        conn.close()
        return sta

    def getinfo(self,name):
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHUSER,(name))
        data=cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def getaccess(self,name):
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHUSERBYID,name)
        data=cursor.fetchone()
        conn.commit()
        conn.close()
        return data[7]

    def serach_all(self):
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHALLUSER,())
        datas=cursor.fetchall()
        conn.commit()
        conn.close()
        return datas

class articles():
    """docstring for ."""
    def create(self,**data):
        conn = init_mysql()
        cursor = conn.cursor()
        sta=cursor.execute(INSERTARTICLE,
                      (data['img'],data['subtitle'],data['author'],data['create'],data['update'],data['title'],data['content'],data['class'],data['counts']))
        conn.commit()
        conn.close()
        return sta

    def count(self,id):
        conn = init_mysql()
        cursor = conn.cursor()
        sta=cursor.execute(COUNTARTICLE,(id))
        conn.commit()
        conn.close()
        return sta

    def delete(self,id):
        conn = init_mysql()
        cursor = conn.cursor()
        sta=cursor.execute(DELETEARTICLE,(id))
        conn.commit()
        conn.close()
        return sta

    def search_one(self,id):
        #:get one article
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHONEARTICLE,(id))
        data=cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def serach_muti(self,data):
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHCLASSARTICLES,(data))
        datas=cursor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def serach_all(self):
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHALLARTICLE,())
        datas=cursor.fetchall()
        conn.commit()
        conn.close()
        return datas

    def update(self,**data):
        conn = init_mysql()
        cursor = conn.cursor()
        sta=cursor.execute(UPDATEARTICLE,(data['img'],data['subtitle'],data['author'],data['update'],data['title'],data['content'],data['class'],data['id']))
        conn.commit()
        conn.close()
        return sta

class comment():
    """docstring for ."""
    def create(self,**data):
        conn = init_mysql()
        cursor = conn.cursor()
        sta=cursor.execute(INSERTCOMMENT,(data['name'],data['content'],data['create'],data['fatherid'],data['sonid'],data['for']))
        conn.commit()
        conn.close()
        return sta

    def search_son(self,id):
        conn=init_mysql()
        cursor=conn.cursor()
        cursor.execute(SEARCHSONCOMMENT,(id))
        data = cursor.fetchall()
        conn.commit()
        conn.close()
        return data

    def search_article(self,id):
        conn=init_mysql()
        cursor=conn.cursor()
        cursor.execute(SEARCHONECOMMENT,(id))
        data = cursor.fetchall()
        conn.commit()
        conn.close()
        return data

    def delete(self,id):
        conn=init_mysql()
        cursor=conn.cursor()
        status=cursor.execute(DELETECOMMENT,(id))
        conn.commit()
        conn.close()
        return status

    def count(self,id):
        conn=init_mysql()
        cursor=conn.cursor()
        status=cursor.execute(COUNTCOMMENT,(id))
        conn.commit()
        conn.close()
        return status

    def serach_all(self):
        conn = init_mysql()
        cursor = conn.cursor()
        cursor.execute(SEARCHALLCOMMENT,())
        datas=cursor.fetchall()
        conn.commit()
        conn.close()
        return datas
