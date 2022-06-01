pipeline {
    agent any
    options {
        disableConcurrentBuilds()
    }
    stages {
        stage ('Building Docker build image') {
            steps {
                script {
                    docker.build("banana-test-image:${GIT_BRANCH}", '--pull .')
                }
            }
        }
        stage ('Checking code quality') {
            steps {
                script {
                    docker.image("banana-test-image:${GIT_BRANCH}").inside() {
                        sh 'cd tests && python3 check_code_quality.py'
                    }
                }
            }
        }
        stage ('Testing Banana') {
            steps {
                script {
                    docker.image("banana-test-image:${GIT_BRANCH}").inside() {
                        sh 'echo -ne "Using VERA VERSION:"; vera++ -version; echo'
                        sh 'cd tests && python3 run_tests.py'
                    }
                }
            }
        }
    }

    post {
        always {
            junit(
                allowEmptyResults: true,
                testResults: 'tests/tests-report.xml'
            )
        }
    }
}
