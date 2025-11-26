pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/<your-repo>.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                docker build -t flask-app .
                '''
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop flask-app
                docker rm flask-app
                docker run -d -p 5000:5000 --name flask-app flask-app
                '''
            }
        }
    }
}
