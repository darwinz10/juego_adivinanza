pipeline {
  agent any

  stages {
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
