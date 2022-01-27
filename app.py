from flask import Flask, flash,render_template,request,redirect,session
from flask import flash
from pymongo import MongoClient


client = MongoClient("mongodb+srv://siddu:valorant6003@cluster0.utg5s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client['Cloudwiry_users']
collection=db.Credentials
db2=client['Cloudwiry_users_files']
collection2=db2.files

Users={'admin':{'password':'admin'}}
app=Flask(__name__)
app.secret_key='123456'



@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/Register.html',methods=['GET'])
def register():
    return render_template('Register.html')

@app.route('/valid',methods=['GET','POST'])
def verify():
    u=request.form.get('username')
    p=request.form.get('password')
    query=collection.find_one({'username':u})
    if query is not None:
        if query['password']==p:
                session['username']=u
                return redirect('success')
        else :
            return redirect('/')
    else:
        return redirect('/')

@app.route('/get',methods=['GET','POST']) 
def get():
    if session['username'] in session:
        s=session['username']
        return render_template('get.html',name=s)
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
        collection2.insert_one({'username':u,'files':[]})
        return redirect('/')
    
@app.route('/success',methods=['GET'])
def success():
    if 'username' in session:
        s=session['username']
        return render_template('success.html',name=s)
    else:
        return redirect('/')

@app.route('/upload',methods=['GET','POST'])
def upload():
    
    if request.method=='POST':
        file=request.files['file']
        query=collection2.find_one({'username':session['username']})
        if query is not None:
            collection2.update_one({'username':session['username']},{'$push':{'files':file.filename}})
            return redirect('/success')
        else:
            return redirect('/success')
    else:
        return render_template('/success')

@app.route('/download',methods=['GET','POST'])
def download():
    query=collection2.find_one({'username':session['username']})
    if query is not None:
        files=query['files'][0]
        return files

@app.route('/logout',methods=['GET'])
def logout():
    session['username']=None
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)