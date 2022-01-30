from flask import Flask,url_for, flash,render_template,request,redirect,session
from flask import flash
from pymongo import MongoClient
import os



client = MongoClient("mongodb+srv://siddu:valorant6003@cluster0.utg5s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client['Cloudwiry_users']
collection=db.Credentials
db2=client['Cloudwiry_users_files']
collection2=db2.files
collection3=db2['fs.files']


app=Flask(__name__)
app.secret_key='123456'
app.config["MONGO_URI"] = "mongodb+srv://siddu:valorant6003@cluster0.utg5s.mongodb.net/Cloudwiry_users_files?retryWrites=true&w=majority"





@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/Register.html',methods=['GET'])
def register():
    return render_template('Register.html')

@app.route('/valid',methods=['GET','POST'])
def verify():
    if request.method=='POST':
        u=request.form.get('username')
        p=request.form.get('password')
        query=collection.find_one({'username':u})
        if query is not None:
            if query['password']==p:
                session["username"]=u
                return redirect("success")
            else :
                return redirect('/')
        else:
            return redirect('/')
    else :
        return redirect('/')

@app.route('/get',methods=['GET','POST']) 
def get():
    if 'username' in session:
        s=session['username']
        return render_template('get.html',name=s)
    else:
        return redirect('/')

app.config['UPLOAD_FOLDER'] = 'static/users'
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
        os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'],u))
        return redirect('/')
    
@app.route("/success")
def success():
    if "username" in session:
        s=session["username"]
        file=[]
        for i in os.listdir(os.path.join(app.config['UPLOAD_FOLDER'],session["username"])):
            file.append(i)

        return render_template('success.html',name=s,x=file)
    else:
        return redirect('/')

@app.route('/upload',methods=['GET','POST'])
def upload():
    
    if request.method=='POST':
        file=request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],session['username'],file.filename))
        return redirect('/success')
    else:
        return render_template('/')

@app.route('/<filename>')
def download(filename):
        return redirect(url_for('static',filename='users/'+session['username']+'/'+filename))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)