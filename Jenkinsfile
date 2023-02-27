pipeline {
  agent any
  environment {
    IMAGE_TAG = "projet:latest"
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build and test feature branches') {
      steps {
        bat 'pip install Backend/requirements.txt'
        bat 'python Backend/app.py'
        bat 'python Backend/test_backend_flask.py'
      }
    }
    stage('Stress test and push to release') {
      steps {
        bat 'docker-compose up --build -d'
        bat 'python StressTest.py'
      }
    }
    stage('Wait for user acceptance on release branch') {
      when {
        branch 'develop'
      }
      steps {
        input message: 'Ready to deploy to main branch?', ok: 'Deploy'
      }
    }
  }
}
