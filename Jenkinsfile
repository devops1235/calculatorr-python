pipeline{
    agent any
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages{
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }
        stage('code-checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/devops1235/calculatorr-python.git'

            }

        }

        stage('code-scanner'){
            environment{
                SONAR_URL = "http://192.168.29.144:9000"
            }
            steps{
                withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_AUTH_TOKEN')]) {
                    sh ''' $SCANNER_HOME/bin/sonar-scanner  -Dsonar.url=${SONAR_URL} -Dsonar.login=${SONAR_AUTH_TOKEN} -Dsonar.projectName=calaculator-app \
                    -Dsonar.source=. \
                    -Dsonar.projectKey=calaculator-app '''
                }

            }

        }

        stage('OWASP Dependency Check'){
            steps{
                dependencyCheck additionalArguments: '--scan ./', odcInstallation: 'DP'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('Build and Test'){
            steps{
                sh 'docker build . -t devopstraning1235/calculator-app:${BUILD_NUMBER}'
            }
        }

        stage('image push to dockerhub'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]){
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh 'docker push devopstraning1235/calculator-app:${BUILD_NUMBER}'
                }
            }
        }

        

        stage('Update Deployment File') {
            environment {
                GIT_REPO_NAME = "calculatorr-python"
                GIT_USER_NAME = "devops1235"
            }
            steps {
                withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]) {
                    sh '''
                        git config user.email "devopstraing159@gmail.com"
                        git config user.name "devops1235"
                        BUILD_NUMBER=${BUILD_NUMBER}
                        sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" manifests/deployment.yml
                        git add manifests/deployment.yml
                        git commit -m "Update image version ${BUILD_NUMBER}"
                        git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                    '''
                }
            }
        }
    }
}
