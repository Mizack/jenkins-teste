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
                    dir("${WORKSPACE}") {
                        sh 'docker compose up -d --build --force-recreate'
                    }
                }
            }
        }

        stage('Testar Rotas Existentes') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        sh 'docker exec docker-jenkins pytest -v'
                    }
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker compose down -v'
        }
    }
}