#!groovy

pipeline {
    agent {
        label 'docker'
    }

    options {
        buildDiscarder(logRotator(daysToKeepStr:'15'))
    }

    stages {
        stage('Build') {
            steps {
                ansiColor('xterm') {
                    sh "docker build -t epitechcontent/vera:latest ."
                }
            }
        }
        stage('Archive') {
            when {
                not {
                    expression {
                        return params.RELEASE
                    }
                }
            }
            steps {
                ansiColor('xterm') {
                    script {
                        docker.withRegistry('https://nexus.epitest.eu:9081/', 'nexus-epitest-ci') {
                            sh "docker tag epitechcontent/vera:latest nexus.epitest.eu:9081/epitechcontent/vera:latest && docker push nexus.epitest.eu:9081/epitechcontent/vera:latest"
                        }
                        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-login') {
                            sh "docker push epitechcontent/vera:latest"
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            withCredentials([string(credentialsId: 'teams-webhook', variable: 'TEAMS_WEBHOOK')]) {
                script {
                    office365ConnectorSend message: "Build Success for $JOB_NAME#$BUILD_ID", status:"Success", webhookUrl:"$TEAMS_WEBHOOK"
                }
            }
        }
        failure {
            withCredentials([string(credentialsId: 'teams-webhook', variable: 'TEAMS_WEBHOOK')]) {
                script {
                    office365ConnectorSend message: "Build Failure for $JOB_NAME#$BUILD_ID", status:"Failure", webhookUrl:"$TEAMS_WEBHOOK"
                }
            }
        }
        always {
            deleteDir()
        }
    }
}
