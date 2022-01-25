from flask import Flask,render_template,request,redirect,session
from flask_session import Session

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/Register.html',methods=['GET'])
def register():
    return render_template('Register.html')

if __name__=="__main__":
    app.run(debug=True)