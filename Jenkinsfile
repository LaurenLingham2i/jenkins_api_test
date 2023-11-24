pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run API Test') {
            steps {
                bat 'python api_test.py'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            bat 'rd /s /q venv'
        }
    }
}
