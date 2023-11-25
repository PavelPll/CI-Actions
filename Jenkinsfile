pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'aws-agent1' }
            steps {
                sh 'sudo apt install docker.io -y'
                sh 'sudo apt install python3-pip -y'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'ls -la'
                sh 'pip3 install -r theProject/requirements.txt'

                sh 'python3 -m py_compile theProject/run.py'
                stash(name: 'compiled-results', includes: 'theProject/*.py*')
            }
        }
        stage('Test') {
            agent { label 'aws-agent1' }
            steps {
                sh 'python3 -m pytest -v --junit-xml test-reports/results.xml ./theProject'
            }
            post {
                always {
                    junit "test-reports/results.xml"
                }
            }
        }
        stage('Deliver') {
            agent { label 'aws-agent1' }
            environment {
                VOLUME = '$(pwd):/src'
                IMAGE = 'cdrx/pyinstaller-linux'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh 'sudo docker image build ../ -t py2bin:latest'
                    sh "sudo docker run --rm -v ${VOLUME} py2bin 'pyinstaller -F --hidden-import numpy --hidden-import tqdm theProject/run.py'"
                }
            }
            post {
                success {
                    archiveArtifacts env.BUILD_ID + "/dist/run"
                }
            }
        }
        
    }
}
