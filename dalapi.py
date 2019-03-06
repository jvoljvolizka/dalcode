#!/usr/bin/python3
from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import subprocess
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def uploade_file():
   return render_template('index.html'),418

@app.route('/encode', methods = ['GET', 'POST'])
def encode_file():
   if request.method == 'POST':
      f = request.files['file']
      f.filename = "yarak"
      f.save(secure_filename(f.filename))
      out = subprocess.check_output("python /root/dalcoder/dalencode.py " + f.filename + " > /root/dalcoder/encoded.dal", shell=True)
      subprocess.call("rm ./" +  f.filename , shell=True)
      return send_file("/root/dalcoder/encoded.dal" , attachment_filename='encoded.dal')

@app.route('/decode', methods = ['GET', 'POST'])
def decode_file():
   if request.method == 'POST':
      f = request.files['file']
      f.filename = "yarak"
      f.save(secure_filename(f.filename))
      out = subprocess.check_output("python /root/dalcoder/daldecode.py " + f.filename + " /root/dalcoder/decoded.dal", shell=True)
      subprocess.call("rm ./" +  f.filename , shell=True)
      return send_file("/root/dalcoder/decoded.dal" , attachment_filename='decoded.dal')
if __name__ == '__main__':
   app.static_folder = 'static'
   app.run(host="0.0.0.0", debug = False)
