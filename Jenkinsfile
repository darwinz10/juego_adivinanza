pipeline {
  agent {
    docker {
      image 'python:3.11'  // Imagen oficial de Python
      args '-v /var/jenkins_home:/var/jenkins_home'  // Opcional: para persistencia
    }
  }

  stages {
    stage('Preparar entorno') {
      steps {
        sh 'python -m venv venv'
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
