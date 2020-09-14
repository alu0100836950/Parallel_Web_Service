from flask import Flask
from flask import render_template, session, redirect, escape, request, url_for, send_file

import json
import os
import subprocess

import time


app = Flask(__name__)


@app.route('/apps')
def apps():
    files =  os.listdir('.')
    apps = []
    
    for f in files:
        if '.exe' in f:
            apps.append(f)

    return json.dumps(apps)


@app.route('/apps/<name>')
def appDetails(name):
    name = name.replace('.exe', '.json')
    with open(name) as f:
        jdata = json.load(f)
    return json.dumps(jdata)


@app.route('/upload', methods = ['POST'])
def upload():
    for file in request.files.getlist('file'):
        file.save(file.filename)
    return 'Imagen subida'


@app.route('/exec/<name>', methods = ['POST'])
def execute(name):
    params = request.get_json()
    print(params)
    if params['algoritmo'] == 'mpi':
        os.popen('mpirun -n ' + str(params['num_cores']) + ' ./mpi.exe ' +  params['input_image'] + ' ' + params['output_image']).read()
    else:
        os.popen('./openmp.exe ' +  params['input_image'] + ' ' + params['output_image']).read()
        # if result == 0:
        #     print('Parece que todo bien')
        # else:
        #     print('Revisar archivo: salida_del_comando.log para tener más detalle')
    
    return send_file(params['output_image'])


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
    #app.run(debug=False)