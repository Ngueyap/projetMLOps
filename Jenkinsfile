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
        bat 'C:/Users/hp/AppData/Local/Programs/Python/Python38/python -m pip install Backend/requirements.txt'
        bat 'python Backend/app.py'
        bat 'python Backend/test_backend_flask.py'
        echo 'g'
      }
    }
    stage('Stress test and push to release') {
      steps {
        bat 'docker-compose up --build -d'
        bat 'python StressTest.py'
        echo 'g' 
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
