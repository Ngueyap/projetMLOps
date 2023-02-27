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
        echo 'g'
      }
    }
    stage('Stress test and push to release') {
      steps {
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
