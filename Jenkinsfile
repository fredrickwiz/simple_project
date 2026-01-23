pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "simple_project_web"
        REGISTRY_ID = "wreckinghang" // Change this
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Builds the image using the Dockerfile provided earlier
                    app = docker.build("${REGISTRY_ID}/${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Runs Django tests inside the container
                    sh "docker run --rm ${REGISTRY_ID}/${DOCKER_IMAGE}:${env.BUILD_ID} python manage.py test"
                }
            }
        }

        stage('Push to Registry') {
            // Only push if tests pass and we are on the main branch
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        app.push()
                        app.push("latest")
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up the local images to save disk space
            sh "docker rmi ${REGISTRY_ID}/${DOCKER_IMAGE}:${env.BUILD_ID} || true"
        }
    }
}
