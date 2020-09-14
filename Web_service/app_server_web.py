from flask import Flask
from flask import render_template, session, redirect, escape, request, url_for, send_file
from flask_login import logout_user, LoginManager
from flask_pymongo import PyMongo
import bcrypt
import requests
from PIL import Image
import io


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'educaweb'
app.config['MONGO_URI'] = 'mongodb+srv://alberto:alberto2019@cluster0.iklun.gcp.mongodb.net/educaweb?retryWrites=true&w=majority'
#app.config['MONGO_URI']= 'mongodb+srv://alberto:alberto@cluster0.goim1.mongodb.net/web_service?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        r = requests.get('http://localhost:5000/apps')
        apps = r.json()
        return render_template('index.html', name=session['username'], apps = apps)
    else:
        return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/exec/<name>', methods = ['POST'])
def exec(name):
    params = request.get_json()
    r = requests.post('http://localhost:5000/exec/' + name, json = params)
    img = Image.open(io.BytesIO(r.content))
    img.save('static/temp/output.jpg')
    return send_file('static/temp/output.jpg')


@app.route('/upload', methods = ['POST'])
def upload():
    for f in request.files.getlist('file'):
        send = {'file':(f.filename, f)}
        response = requests.post('http://localhost:5000/upload', files = send)
    return response.text



@app.route('/form/<name_file>')
def form(name_file):
    r = requests.get('http://localhost:5000/apps/' + name_file)
    data = r.json()
    ok = 'ok'
    return render_template('form.html', data = data, ok = ok)


@app.route('/login', methods= ['POST'])
def logueo():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username or password'



app.secret_key = 'mysecret'



if __name__ == '__main__':
    app.run('127.0.0.1', 4000, debug=True)
    #app.run(debug=False)