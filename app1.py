                                #Discussion board
''' installing all the packages that are needed to our project'''
from flask import Flask,redirect,render_template,request,url_for,session,flash,send_file
from flask_session import Session 
from flask_mysqldb import MySQL
from io import BytesIO      # the files in the form of bytes
import io
from itsdangerous import URLSafeTimedSerializer

#from tokenreset import token1
from stoken import token
from cmail import sendmail
from key import secret_key,salt1,salt2
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from stoken1 import token
import random
app=Flask(__name__)
app.secret_key = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nazeer@786'
app.config['MYSQL_DB'] = 'forum'
Session(app)
mysql = MySQL(app)
@app.route('/') 
def index():
    return render_template('index.html')
@app.route('/registration', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
       
        name = request.form['name']
        
        password = request.form['password']
        email = request.form['email']
        
        
        cursor = mysql.connection.cursor()
       
        cursor.execute ('select email from users')
        edata = cursor.fetchall()
        cursor.execute ('select username from users')
        ename=cursor.fetchall() 
        if (name,)in ename:
            flash('user already exits')                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            return render_template('register.html')
        if (email,)in edata:
            flash('email already exits')                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            return render_template('register.html')
        cursor.close()
        data={'username':name,'password':password,'email':email}
        subject='Email Confirmation'
        body=f"Thanks for signing up\n\nfollow this link for further steps-{url_for('confirm',token=token(data,salt1),_external=True)}"
        sendmail(to=email,subject=subject,body=body)
        flash('confirmation link sent to mail')
        return redirect(url_for('login'))
    return render_template('register.html')
@app.route('/confirm/<token>')
def confirm(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        data=serializer.loads(token,salt=salt1,max_age=180)
    except Exception as e:
      
        return 'Link Expired register again'
    else:
        cursor=mysql.connection.cursor()
        username=data['email']
        cursor.execute('select count(*) from users where email=%s',[username])
        count=cursor.fetchone()[0]
        if count==1:
            cursor.close()
            flash('You are already registerterd!')
            return redirect(url_for('login'))
        else:
            cursor.execute('insert into users values(%s,%s,%s)',[data['username'],data['email'],data['password']])
            mysql.connection.commit()
            cursor.close()
            flash('Details registered!')
            return redirect(url_for('login'))
@app.route('/login',methods =['GET','POST'])
def login():
    if session.get('user'):
        return redirect(url_for('availableposts'))
    if request.method == 'POST':
        rollno = request.form['id']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('select count(*) from users where email=%s and password=%s',[rollno,password])#if the count is 0 then either username or password is wrong or if it is 1 then it is login successfully
        count = cursor.fetchone()[0]
        if count == 0:
            flash('Invalid username or password')
            return render_template('login.html')
        else:
            session['user'] = rollno
            return redirect(url_for('availableposts'))
    return render_template('login.html')
@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        flash('user Successfully logged out')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
@app.route('/aregistration', methods = ['GET','POST'])
def aregister():
    if request.method == 'POST':
       
        name = request.form['name']
        
        password = request.form['password']
        email = request.form['email']
        
        
        cursor = mysql.connection.cursor()
       
        cursor.execute ('select email from admin')
        edata = cursor.fetchall()
        cursor.execute ('select username from admin')
        ename = cursor.fetchall() 
        if(name,) in ename:
            flash('email already exits')                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            return render_template('adminregister.html')
        if (email,)in edata:
            flash('email already exits')                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            return render_template('adminregister.html')
        cursor.close()
        data1={'username':name,'password':password,'email':email}
        subject='Email Confirmation'
        body=f"Thanks for signing up\n\nfollow this link for further steps-{url_for('aconfirm',token=token(data1,salt1),_external=True)}"
        sendmail(to=email,subject=subject,body=body)
        flash('confirmation link sent to mail')
        return redirect(url_for('alogin'))
    return render_template('adminregister.html')
@app.route('/aconfirm/<token>')
def aconfirm(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        data1=serializer.loads(token,salt=salt1,max_age=180)
    except Exception as e:
   
        return 'Link Expired register again'
    else:
        cursor=mysql.connection.cursor()
        username=data1['email']
        cursor.execute('select count(*) from admin where email=%s',[username])
        count=cursor.fetchone()[0]
        if count==1:
            cursor.close()
            flash('You are already registerterd!')
            return redirect(url_for('alogin'))
        else:
            cursor.execute('insert into admin values(%s,%s,%s)',[data1['username'],data1['email'],data1['password']])
            mysql.connection.commit()
            cursor.close()
            flash('admin Details registered!')
            return redirect(url_for('alogin'))
@app.route('/alogin',methods =['GET','POST'])
def alogin():
    if session.get('admin'):
        return redirect(url_for('addpost'))
    if request.method == 'POST':
        rollno = request.form['id']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('select count(*) from admin where email=%s and password=%s',[rollno,password])#if the count is 0 then either username or password is wrong or if it is 1 then it is login successfully
        count = cursor.fetchone()[0]
        if count == 0:
            flash('admin Invalid username or password')
            return render_template('adminlogin.html')
        else:
            session['admin'] = rollno
            return redirect(url_for('allposts'))
    return render_template('adminlogin.html')
@app.route('/aforget',methods=['GET','POST'])
def aforgot():
    if request.method=='POST':
        email=request.form['id']
        cursor=mysql.connection.cursor()
        cursor.execute('select count(*) from admin where email=%s',[email])
        count=cursor.fetchone()[0]
        cursor.close()
        if count==1:
            
            subject='Forget Password'
            confirm_link=url_for('areset',token=token(email,salt=salt2),_external=True)
            body=f"Use this link to reset your password-\n\n{confirm_link}"
            sendmail(to=email,body=body,subject=subject)
            flash('Reset link sent check your email')
            return redirect(url_for('alogin'))
        else:
            flash('Invalid email id')
            return render_template('forgot.html')
    return render_template('forgot.html')
@app.route('/areset/<token>',methods=['GET','POST'])
def areset(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        email=serializer.loads(token,salt=salt2,max_age=180)
    except:
        abort(404,'Link Expired')
    else:
        if request.method=='POST':
            newpassword=request.form['npassword']
            confirmpassword=request.form['cpassword']
            if newpassword==confirmpassword:
                cursor=mysql.connection.cursor()
                cursor.execute('update admin set password=%s where email=%s',[newpassword,email])
                mysql.connection.commit()
                flash('Reset Successful')
                return redirect(url_for('alogin'))
            else:
                flash('Passwords mismatched')
                return render_template('newpassword.html')
        return render_template('newpassword.html')
    


@app.route('/alogout')
def alogout():
    if session.get('admin'):
        session.pop('admin')
        flash('admin Successfully logged out')
        return redirect(url_for('alogin'))
    else:
        return redirect(url_for('alogin'))
    



@app.route('/allposts')
def allposts():
    if session.get('admin'):
        aid= session.get('admin')
        cursor = mysql.connection.cursor()
        cursor.execute('select * from post where email = %s',[aid])
        notes_data=cursor.fetchall()
        cursor.close()
        return render_template('allposts.html',data = notes_data)
    else:
        return redirect(url_for('alogin'))

@app.route('/addpost',methods = ['GET','POST'])
def addpost():
    if session.get('admin'):
        if request.method == 'POST':
            title = request.form['title']
            content=request.form['content']
            cursor=mysql.connection.cursor()
            id1=session.get('admin')
            cursor.execute('insert into post(email,title,content) values (%s,%s,%s)',[id1,title,content])
            mysql.connection.commit()
            cursor.close()
            flash(f'{title} added successfully')
            return redirect (url_for('allposts'))
        
        else:
            rollno = session.get('admin')
            cursor=mysql.connection.cursor()
            cursor.execute('select * from post where email = %s',[rollno])
            notes_data=cursor.fetchone()
      
        return render_template('post.html',notes_data=notes_data)
        
    else:
        return redirect(url_for('login'))
    
@app.route('/viewpost/<nid>',methods=['GET','POST'])
def viewpost(nid):
    if session.get('admin'):
        cursor=mysql.connection.cursor()

        cursor.execute('select * from post where pid=%s',[nid])
        data=cursor.fetchone()
        return render_template('postview.html',data=data)
    else:
        return redirect(url_for('alogin'))   

@app.route('/availableposts',methods=['GET','POST'])
def availableposts():
    if session.get('admin') or session.get('user'):
        cursor=mysql.connection.cursor()
        cursor.execute('select pid,title,content from post ' )

        data=cursor.fetchall()
   
       
        return render_template('availableposts.html',data=data)

@app.route('/updatepost/<nid>',methods=['GET','POST'])
def updatepost(nid):
    if session.get('admin'):
        cursor=mysql.connection.cursor()
        cursor.execute('select title,content from post where pid=%s',[nid])
        data=cursor.fetchone()
        cursor.close()
        if request.method=='POST':
            title=request.form['title']
            content=request.form['content']
            cursor=mysql.connection.cursor()
            cursor.execute('update post set title=%s,content=%s where pid=%s',[title,content,nid])
            mysql.connection.commit()
            cursor.close()
            flash('post updated successfully')
            return redirect(url_for('allposts'))
        return render_template('updatepost.html',data=data)
    else:
        return redirect(url_for('login'))

@app.route('/deletepost/<nid>')
def deletepost(nid):
    cursor=mysql.connection.cursor()
    cursor.execute('delete from post where pid=%s',[nid])
    mysql.connection.commit()
    cursor.close()
    flash('post deleted successfully')
    return redirect(url_for('allposts'))
#---------------------------------------- posts,comments,replys
@app.route('/comment/<pid>',methods=['GET','POST'])
def comment(pid):
    if session.get('user'):
        cursor = mysql.connection.cursor()
        
        cursor.execute('select a.cid,a.postid,a.email,a.comment,a.date,b.reply,b.cid from comments as a left join reply as b on a.cid=b.cid where a.email=%s and a.postid=%s',[session.get('user'), pid]);
        sender = cursor.fetchall()
        if request.method=="POST":
            message=request.form['message']
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO comments(postid, email, comment) VALUES (%s, %s, %s)', [pid,session['user'], message])
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('availableposts'))
        return render_template('message.html', id=pid, sender=sender)

    else:
        return redirect(url_for('login'))
#--------------------------------------- reply
@app.route('/reply/<id1>',methods=['GET','POST'])
def reply(id1):
    if session.get('user'):
        if request.method == 'POST':
            reply = request.form['reply']
            reply_to = id1
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO reply (reply,cid) VALUES (%s, %s)', [reply,reply_to])
            mysql.connection.commit()
            return redirect(url_for('availableposts'))

    else:
        return redirect(url_for('login'))


        
#------------------------------------------------------------------
@app.route('/forget',methods=['GET','POST'])
def forgot():
    if request.method=='POST':
        email=request.form['id']
        cursor=mysql.connection.cursor()
        cursor.execute('select count(*) from users where email=%s',[email])
        count=cursor.fetchone()[0]
        cursor.close()
        if count==1:
            subject='Forget Password'
            confirm_link=url_for('reset',token=token(email,salt=salt2),_external=True)
            body=f"Use this link to reset your password-\n\n{confirm_link}"
            sendmail(to=email,body=body,subject=subject)
            flash('Reset link sent check your email')
            return redirect(url_for('login'))
        else:
            flash('Invalid email id')
            return render_template('forgot.html')
    return render_template('forgot.html')


@app.route('/reset/<token>',methods=['GET','POST'])
def reset(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        email=serializer.loads(token,salt=salt2,max_age=180)
    except:
        abort(404,'Link Expired')
    else:
        if request.method=='POST':
            newpassword=request.form['npassword']
            confirmpassword=request.form['cpassword']
            if newpassword==confirmpassword:
                cursor=mysql.connection.cursor()
                cursor.execute('update users set password=%s where email=%s',[newpassword,email])
                mysql.connection.commit()
                flash('Reset Successful')
                return redirect(url_for('login'))
            else:
                flash('Passwords mismatched')
                return render_template('newpassword.html')
        return render_template('newpassword.html')   

if __name__ == "__main__":
    app.run(use_reloader=True,debug=True)
    


























