#from __future__ import print_function # Only Python 2.x
from random import random
from subprocess import Popen, PIPE, CalledProcessError
import threading
import time
from flask import Flask,render_template,request
import infoga
import os






app = Flask(__name__) #static_folder="static/assets"



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/idea")
def idea():
    return render_template('idea.html')

@app.route("/approach")
def approach():
    return render_template('approach.html')

@app.route("/details")
def details():
    return render_template('details.html')
#api for executing the SimplyEmail query
#api.add_resource(simplyEmail, '/crawler/<search_term>/')

@app.route("/discovery")
def discovery():
    return render_template('discovery.html')
#thread = threading.Thread(target=background_calculation)
#thread.start()
@app.route('/', methods=['POST'])
def beginToCrawl():
	if request.method == 'POST':
            emailid = request.form['Email']
            str(emailid)

            #cmd = "python infoga.py -b -i "+emailid+" -r discovery.html"
            cmd = "python infoga.py -b -i "+emailid+" -v 3  -r discovery.html"
            crawler = os.popen(cmd)

            discoveries = crawler.read()



            print(discoveries)

            return render_template('discovery.html')



if __name__ == '__main__':
	 app.run(host='0.0.0.0', port=4010, debug=True)
