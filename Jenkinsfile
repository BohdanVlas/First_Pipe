pipeline {
    options{timestamps()}

    agent none
    stages {
        stage('Check scm'){
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build'){
            steps{
                echo "Building ...${BUILD_NUMBER}"
                echo "Build complete"
            }
        }
        stage('Test'){
            steps{
                sh 'apk add --update python3 py-pip'
                sh 'pip install Flask'
                sh 'pip install xmlrunner'
                sh 'python3 Lab3_Test.py'
            }
            post{
                always{
                    junit 'test-reports/*.xml'
                }
                success{
                    echo "Testing successfully completed"
                }
                failure{
                    echo "Testing failed"
                }
            }
        }
    }
}