pipeline {
  agent any
  environment {
    IMAGE_TAG = "ci-docker:latest"
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build and test feature branches') {
      when {
        branch 'back'
      }
      steps {
        bat 'python app.py &'
        bat 'python test_backend_flask.py'
        bat 'pkill -f "python app.py"'
      }
    }
    stage('Stress test and push to release') {
      when {
        branch 'develop'
      }
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
    stage('Push to Dockerhub on merge to main') {
      when {
        branch 'main'
        changeset '.*'
      }
      steps{
        
      }
    }
  }
}
