pipeline {
    agent any
	environment {
		DOCKERHUB_CREDENTIALS = credentials('maximdesign-dockerhub')
		docker_run_check = 0
	}
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/maxim-design/WorldOfGames.git']]])
				script{
					if (isUnix()){
						sh "cat wog.txt"
					}
					else {
						bat "type wog.txt"  
					}
				}
			}
		}
        stage('Build Docker Image') {
            steps {
				script{
					if (isUnix()==true) {
						sh "docker-compose build"
						echo "Docker build complete"
					}
					else {
						bat "docker-compose build"
						echo "Docker build complete"
					}
				}
            }
        }
        stage('Docker UP') {
            steps {
				script{
					if (isUnix()==true) {
						sh "docker-compose up -d"
						echo "Docker Container is running! Flask online."
						docker_run_check = 1
					}
					else {
						bat "docker-compose up -d"
						echo "Docker Container is running! Flask online."
						docker_run_check = 1
						
					}
				}
            }
		}
		stage('Selenium Tesing') {
			steps {
				script {
					if (isUnix()==true) {
						sh "pip install selenium"
						sh "python3 tests//e2e.py"

					}
					else {
						bat "pip install selenium"
						bat "cd tests"
						bat "python tests//e2e.py"
					}
				}
			}
		}
		stage('docker login & push') {
            steps {
				script{
					if (isUnix()==true) {
						sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
						sh 'docker push maximdesign/max-wog'
						
					}
					else {
						bat 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
						bat 'docker push maximdesign/max-wog'
						
					}
				}
            }
		}
	}
	post {
		always {
			script{
				if (isUnix()==true) {
					sh "docker stop WorldOfGames_Platform"
					sh "docker rm WorldOfGames_Platform"
					sh "docker rmi maximdesign/max-wog"
					echo "Docker Container has been terminated & removed."
					sh 'docker logout'
					echo "Logged out of Dockerhub"
				}
				else{
					bat "docker stop WorldOfGames_Platform"
					bat "docker rm WorldOfGames_Platform"
					bat "docker rmi maximdesign/max-wog"
					echo "Docker Container has been terminated & removed."
					bat 'docker logout'
					echo "Logged out of Dockerhub"
				}
			}
		}
	}
}
