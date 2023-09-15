# GUVI-requirement-for-internship
created a simple Python Flask web application.

Install Necessary Tools:

need Python and Flask-

#installed Flask using pip : 

$pip install Flask

#phython 3 installtion

$sudo apt update

$sudo apt install python3

$python3 --version

phython 3 is installed


#Created  a Directory for my project and navigate into:

$mkdir my-web-app
$cd my-web-app

#Create the Web Application:
Created a Python file 

$vi app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello GUVI GEEK networks this is MANIKANTARAJU DIBBIDI D07 DEVOPS GUVI"

if __name__ == '__main__':
    # Listen on all available network interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)

:wq
saved above file
then
#run the above file

$python3 app.py

successfully running state .

#for  output  search with ec2 instance ip address+port (http://3.81.161.151:5000) the application is running state

(http://3.81.161.151:5000)
application running state

#Log In to GitHub:
Created a New Repository: 
GUVI-requirement-for-internship
Initialize with a README file:





 
