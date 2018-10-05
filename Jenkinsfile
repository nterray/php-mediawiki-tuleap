pipeline {
    agent {
        dockerfile {
            label 'docker'
        }
    }

    stages {
        stage('Fetch sources') {
            steps {
                checkout scm
            }
        }
        stage('Check compatibility') {
            steps {
                sh 'phpcs -d memory_limit=-1 --standard=PHPCompatibility  --runtime-set testVersion 7.2 --report-checkstyle=checkstyle.xml --extensions=php mediawiki-1.23.9 || true'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'checkstyle.xml', excludes: null
            checkstyle pattern: 'checkstyle.xml', unstableTotalAll: '0', usePreviousBuildAsReference: true
        }
    }
}
