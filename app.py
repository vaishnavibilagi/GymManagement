from flask import *
from flask import request
import mysql.connector as mysql
app=Flask(__name__)
@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-control']='no-store,max-age=0'
    return response    
app.secret_key="xyz"
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login.html')    
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/user',methods=['POST'])
def user(): 
    firstname=request.form['firstname'] 
    lastname=request.form['lastname']
    password=request.form['password']
    address=request.form['address']
    Email=request.form['Email']
    mobilenumber=request.form['mobilenumber'] 
    dateofbirth=request.form['dateofbirth']
    con=mysql.connect(host='localhost',user='root',password='',database='adms')                     
    cur=con.cursor()
    cur.execute('insert into users values(%s,%s,%s,%s,%s,%s,%s)',(firstname,lastname,password,address,Email,mobilenumber,dateofbirth))
    con.commit()
    con.close()
    flash('data saved')
    return render_template('register.html')
@app.route('/checkuser',methods=['POST'])
def checkuser():
    firstname=request.form['firstname']
    password=request.form['password'] 
    con=mysql.connect(host='localhost',user='root',password='', database='adms')
    cur=con.cursor()
    cur.execute('select * from users where firstname=%s and password=%s',(firstname,password))
    result=cur.fetchall()
    con.close() 
    if(len(result)==0):
        flash('invalid username or password')
        return render_template('login.html')
    else:
        session["firstname"]=firstname
        return render_template('gym.html') 
 

@app.route('/register1')
def register1():
    return render_template('register1.html') 
@app.route('/coach')
def coach():
    return render_template('coach.html')  
@app.route('/plans')
def plans():
    return render_template('plans.html')
@app.route('/display')
def display():
    return redirect('/reg1')    
@app.route('/reg',methods=['POST'])
def reg(): 
    fullname=request.form['fullname'] 
    height=request.form['height']
    weight=request.form['weight']
    address=request.form['address']
    Email=request.form['Email']
    mobilenumber=request.form['mobilenumber'] 
    dateofbirth=request.form['dateofbirth']
    con=mysql.connect(host='localhost',user='root',password='',database='register')                     
    cur=con.cursor()
    cur.execute('insert into regg values(%s,%s,%s,%s,%s,%s,%s)',(fullname,height,weight,address,Email,mobilenumber,dateofbirth))
    con.commit()
    con.close()
    flash('date saved')
    return redirect('/register1')    
@app.route('/reg1') 
def reg1():
    con=mysql.connect(host='localhost',user='root',password='',database='register')                     
    cur=con.cursor()
    cur.execute('select * from regg')
    result=cur.fetchall()
    con.close()
    return render_template('display.html',regg=result) 
@app.route('/edituserform<name>')
def edituserform(name):
    con=mysql.connect(host='localhost',user='root',password='',database='register')
    cur=con.cursor()
    cur.execute('select * from regg where fullname=%s',(name,))
    result=cur.fetchone()
    con.close()
    return render_template('edituser.html',regg=result)   
@app.route('/updateuser',methods=['POST'])
def updateuser():
    fullname=request.form['fullname'] 
    height=request.form['height']
    weight=request.form['weight']
    address=request.form['address']
    Email=request.form['Email']
    mobilenumber=request.form['mobilenumber'] 
    dateofbirth=request.form['dateofbirth'] 
    con=mysql.connect(host='localhost',user='root',password='',database='register')
    cur=con.cursor()
    cur.execute('update regg set fullname=%s,height=%s,weight=%s,address=%s,Email=%s,mobilenumber=%s,dateofbirth=%s where fullname=%s',(fullname,height,weight,address,Email,mobilenumber,dateofbirth,fullname))   
    con.commit()
    if(cur.rowcount>0):
        flash('data updated succesfully')
    else:
        flash('unable to update')
    con.close()
    return redirect('/display')
@app.route('/deleteuser<name>')
def deleteuser(name):
    con =mysql.connect(host='localhost',user='root',password='',database='register')
    cur=con.cursor()
    cur.execute('delete from regg where fullname=%s',(name,))   
    con.commit()
    if(cur.rowcount>0):
        flash('data deleted succesfully')
    else:
        flash('unable to delete data')
    con.close()
    return redirect('/display') 
@app.route('/searchuser')
def searchuser():
    fullname=request.args.get('fullname')
    print(fullname)
    con=mysql.connect(host='localhost',user='root',password='',database='register')  
    cur=con.cursor()
    cur.execute('select * from regg where fullname=%s',(fullname,))
    result=cur.fetchall()
    if(len(result)==0):
        flash('user not found')
        return render_template('display.html',regg=[])
    else:
        return render_template('display.html',regg=result) 
@app.route('/logout')
def logout():
    session.pop('firstname') 
    return render_template('login.html')             
      




       



     

        