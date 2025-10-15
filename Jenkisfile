pipeline {
    agent any
    stages {
        stage('Limpiar Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Clonar Repositorio') {
            steps {
                withCredentials([string(credentialsId: 'GitHub', variable: 'TOKEN')]) {
                    sh '''
                        git clone -b master https://$TOKEN@github.com/Yazmin0709/practica.git
                        cd practica
                        ls -l
                    '''
                }
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-venv
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pytest
                '''
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh '''
                    . venv/bin/activate
                    cd practica
                    pytest test.py
                '''
            }
        }
    }
    post {
        always { echo 'Pipeline completado' }
        success { echo 'El pipeline fue exitoso' }
        failure { echo 'El pipeline falló' }
    }
}
