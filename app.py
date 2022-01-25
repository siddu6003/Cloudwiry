from flask import Flask, flash,render_template,request,redirect,session
from flask import flash

Users={'admin':{'password':'admin'}}
app=Flask(__name__)
app.secret_key='123456'

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

    if u in Users:
        if Users[u]['password']==p:
            session['username']=u
            return redirect('success')
    else:
        return redirect('/')

@app.route('/register',methods=['POST','GET'])
def register_user():
    u=request.form.get('username')
    p=request.form.get('password')
    if u in Users:
        return redirect('/Register.html')
    else:
        Users[u]={'password':p}
        return redirect('/')
    
@app.route('/success',methods=['GET'])
def success():
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)