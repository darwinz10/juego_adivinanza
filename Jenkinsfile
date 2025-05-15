pipeline {
  agent any

  stages {
    stage('Instalar Python si no está') {
      steps {
        sh 'which python3 || sudo apt update && sudo apt install -y python3 python3-pip python3-venv'
      }
    }

    stage('Preparar entorno') {
      steps {
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate && pip install -r requirements.txt'
      }
    }

    stage('Ejecutar pruebas') {
      steps {
        sh '. venv/bin/activate && pytest'
      }
    }
  }

  post {
    success {
      echo '✔️ Pruebas exitosas.'
    }
    failure {
      echo '❌ Las pruebas fallaron.'
    }
  }
}
