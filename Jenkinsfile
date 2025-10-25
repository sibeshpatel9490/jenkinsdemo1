pipeline {
    agent any 
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Extract Data') {
            steps {
                bat "python extract.py"
            }
        }
    }
}