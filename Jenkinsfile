pipeline {
    agent {
        kubernetes {
            label 'data-pipeline-agent'
            defaultContainer 'python-container'
        }
    }
    environment {
        requirements = fileExists './requirements.txt'
    }
    stages {
        stage('PR Analyze') {
            when {
                environment name: 'PR_ANALYZE', value: 'true'
                expression { requirements == 'true' }
            }
            steps {
                stepGithubStatus() {
                    stepTrack(PROJECT: env.PROJECT) {

                        sh """
                            pip install -r requirements.txt
                            pip install pylint
                            pip install flake8
                            flake8 .
                        """
                    }
                }
            }
        }
    }
}

