pipeline {
  agent any

  stages {
    stage('Hola') {
      steps {
        echo '✅ ¡El pipeline está funcionando!'
      }
    }
  }

  post {
    success {
      echo '✔️ Todo funcionó correctamente.'
    }
    failure {
      echo '❌ Hubo un error en el pipeline.'
    }
  }
}
