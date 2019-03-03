from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import subprocess
app = Flask(__name__)

@app.route('/')
def uploade_file():
   return render_template('index.html'),418

@app.route('/encode', methods = ['GET', 'POST'])
def encode_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      out = subprocess.check_output("python ./dalencode.py " + f.filename + " > encoded.dal", shell=True)
      subprocess.call("rm ./" +  f.filename , shell=True)
      return send_file("encoded.dal" , attachment_filename='encoded.dal')

@app.route('/decode', methods = ['GET', 'POST'])
def decode_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      out = subprocess.check_output("python ./daldecode.py " + f.filename + " decoded.dal", shell=True)
      subprocess.call("rm ./" +  f.filename , shell=True)
      return send_file("decoded.dal" , attachment_filename='decoded.dal')
if __name__ == '__main__':
   app.run(host="0.0.0.0", debug = True)
