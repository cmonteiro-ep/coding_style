pipeline {
    agent any
    options {
        disableConcurrentBuilds()
    }
    stages {
        stage ('Building Docker build image') {
            steps {
                script {
                    docker.build("banana-test-image:master", '--pull .')
                }
            }
        }
        stage ('Testing Banana') {
            steps {
                script {
                    docker.image("banana-test-image:master").inside("""--entrypoint=''""") {
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
