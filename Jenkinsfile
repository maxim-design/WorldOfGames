pipeline {
    agent any
	environment {
		DOCKERHUB_CREDENTIALS = credentials('maximdesign-dockerhub')
	}
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/maxim-design/WorldOfGames.git']]])
		if (isUnix()){
			sh "type wog.txt"
                   }
                else {
                    	bat "type wog.txt"  
                   }
            }
        }
        stage('Build Docker Image') {
            steps {
				if (isUnix()) {
					sh "docker-compose build"
					echo "Docker build complete"
				}
				else {
					bat "docker-compose build"
					echo "Docker build complete"
				}
            }
        }
        stage('Docker UP') {
            steps {
                if (isUnix()) {
					sh "docker-compose up -d"
					echo "Docker Container is running! Flask online."
				}
				else {
					bat "docker-compose up -d"
					echo "Docker Container is running! Flask online."
				}
            }
		}
		stage('Selenium Tesing') {
            steps {
				if (isUnix()) {
					sh "pip install selenium"
					sh "cd test; python3 e2e.py;"
					if ( $? -eq 0 ) then {set -o errexit}
					else {echo "Testing Successful"}
					sh "cd .."

				}
				else {
					bat "pip install selenium"
					bat "cd test & python3 e2e.py"
					if %ERRORLEVEL% EQU 1 echo (exit /b 1)
					if %ERRORLEVEL% EQU 0 echo "Testing Successful"
					bat "cd .."
				}
			}
		}
		stage('docker login & push') {
            steps {
                if (isUnix()) {
					sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
					
				}
				else {
					bat "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
					
				}
            }
			steps {
				if (isUnix()) {
					sh "docker push maximdesign/max-wog"
					
				}
				else {
					bat "docker push maximdesign/max-wog"
				}
			}
		}
		stage('docker stop and remove') {
            steps {
                if (isUnix()) {
					sh "docker stop WorldOfGames_Platform"
					sh "docker rm WorldOfGames_Platform"
					sh "docker rmi maximdesign/max-wog"
					echo "Docker Container has been terminated & removed."
				}
				else {
					bat "docker stop WorldOfGames_Platform"
					bat "docker rm WorldOfGames_Platform"
					bat "docker rmi maximdesign/max-wog"
					echo "Docker Container has been terminated & removed."
				}
            }
		}
	post {
        always {
            if (isUnix()) {
				sh 'docker logout'
				echo "Logged out of Dockerhub"
			}
			else{
				bat 'docker logout'
				echo "Logged out of Dockerhub"
			}
        }
    }
}
