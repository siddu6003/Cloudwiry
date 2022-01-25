from flask import Flask, flash,render_template,request,redirect,session
from flask import flash
from pymongo import MongoClient


client = MongoClient("mongodb+srv://siddu:valorant6003@cluster0.utg5s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client['Cloudwiry_users']
collection=db.Credentials
result=collection.find_one({'username':'admin'})
res=result['password']

Users={'admin':{'password':'admin'}}
app=Flask(__name__)
app.secret_key='123456'

@app.route('/dbquery')
def dbquery():
    return str(res)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/Register.html',methods=['GET'])
def register():
    return render_template('Register.html')

@app.route('/session',methods=['GET','POST'])
def verify():
    u=request.form.get('username')
    p=request.form.get('password')
    query=collection.find_one({'username':u})
    if query is not None:
        if query['password']==p:
            return redirect('success')
        else :
            return redirect('/')
    else:
        return redirect('/')

@app.route('/register',methods=['POST','GET'])
def register_user():
    u=request.form.get('username')
    p=request.form.get('password')
    query=collection.find_one({'username':u})
    if query is not None:
        return redirect('/Register.html')
    else:
        collection.insert_one({'username':u,'password':p})
        return redirect('/')
    
@app.route('/success',methods=['GET'])
def success():
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)