pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-web-app .'
            }
        }
        stage('Publish to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'manikantaraju', passwordVariable: 'Likhitha@2004')]) {
                    sh "docker login -u $manikantaraju-p $Likhitha@2004"
                    sh "docker tag my-web-app manikantaraju/my-web-app:latest"
                    sh "docker push manikantaraju/my-web-app:latest"
                }
            }
        }
    }
}
