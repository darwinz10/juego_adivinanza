pipeline {
  agent any

  stages {
    stage('Verificar Python') {
      steps {
        // Si python3 no está, lo notifica
        sh '''
          if ! command -v python3; then
            echo "❌ Python3 no está instalado en Jenkins. Debes instalarlo manualmente en el contenedor Jenkins."
            exit 1
          fi
        '''
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
