pipeline {
    agent any
    
    stages {
        stage('Construir Imagem Docker') {
            steps {
                script {
                    def dockerImage = 'miza14/docker-jenkins:1.0'
                    docker.build(dockerImage)
                }
            }
        }
        stage('Executar Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
    
    post {
        always {
            // Remova os containers e volumes após a execução da pipeline
            cleanWs()
            script {
                sh 'docker-compose down -v'
            }
        }
    }
}