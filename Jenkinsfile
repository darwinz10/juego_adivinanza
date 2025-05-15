pipeline {
  agent any

  stages {
    stage('Preparar entorno') {
      steps {
        // Crear entorno virtual
        bat 'python -m venv venv'
        // Activar entorno e instalar dependencias
        bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
      }
    }

    stage('Ejecutar pruebas') {
      steps {
        // Activar entorno y ejecutar pytest
        bat '.\\venv\\Scripts\\activate && pytest'
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
