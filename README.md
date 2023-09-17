### docker hub:
manikantaraju/guvi-intern

above my docker-hub-username/repository-name






# GUVI-requirement-for-internship
created a simple Python Flask web application.

Install Necessary Tools:

need Python and Flask-

#installed Flask using pip : 

$pip install flask

#phython 3 installtion

$sudo apt update

$sudo apt install python3

$python3 --version

phython 3 is installed


#Created  a Directory for my project and navigate into:

$mkdir my-web-app
$cd my-web-app

### step 1 :
Create the Web Application:
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

### step 2 : log In to GitHub:

Created a New Repository: 
GUVI-requirement-for-internship

Initialize with a README file:

$git clone (repo url)

$git init

$git add .

$git commit -m "commiting"

$git push origin main
 #successfully pushed into central repo
 
 ### Step 3: Configure Jenkins
 
 1. Set up Jenkins on my AWS EC2 instance.
2. Create a Jenkins job to build my web application.
3. Configure Jenkins to listen for webhook events from my GitHub repository.

 ### Step 4: Create a Jenkins Pipeline

1. Use Pipeline as Code (Jenkinsfile) to define  build and deployment steps.
2. Define the pipeline stages, including cloning the repository, building the code, and creating a Docker image.

### Step 5: Build Docker Image

1. During the Jenkins job execution, the defined pipeline will build my web application code.
2. A Docker image of my application will be created using the Docker plugin in Jenkins.

### Step 6: Push to Docker Hub

1. After successful image build, Jenkins will use Docker to push the image to Docker Hub.
2. Docker Hub credentials configured in Jenkins for this step.

### Step 7: Monitor Jenkins Job

1. Monitor the Jenkins job's console output to ensure each step of the pipeline executes successfully.
2. Look for any errors or issues during the build and deployment process.

### Step 8: Verify Docker Hub

1. Log in to Docker Hub and verify that the Docker image  web application has been pushed 







  

 






 
