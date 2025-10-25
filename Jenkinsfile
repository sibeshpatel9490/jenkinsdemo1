node {
    def PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'

    try {
        stage('Checkout') {
            checkout scm
        }

        stage('Setup Python') {
            bat "${PYTHON} --version"
        }

        stage('Extract Data') {
            bat "${PYTHON} extract.py"
        }

    } catch (err) {
        echo "Pipeline failed: ${err}"
        currentBuild.result = 'FAILURE'
    } finally {
        echo 'Pipeline completed.'
    }
}
