pipeline {
	agent any
	
	triggers {
        cron('H 09 * * 1-7')
    }
	
	stages{
		stage ('Clean Stage') {
			steps {
				withMaven(maven:'M2_HOME'){
				    
					sh 'mvn clean '
				}
			}
		}
		
		stage ('Compile Stage') {
			steps {
				withMaven(maven:'M2_HOME'){
					sh 'mvn compile'
				}
			}
		}
		
		stage ('SonarQube Analysis') {
			steps {
				withMaven(maven:'M2_HOME'){
				   sh 'mvn sonar:sonar -Dsonar.login=12eaff0b9d179849f2cfcb2dd9a5f15fa9c68a06  -Dsonar.host.url=http://10.253.84.109:9000/sonar'
				}
			}
		}
		
		stage ('Test Stage') {
			steps {
				withMaven(maven:'M2_HOME'){
					sh 'mvn test'
				}
			}
		}
		
		stage ('Build Stage') {
			steps {
				withMaven(maven:'M2_HOME'){
					sh 'mvn install'
				}
			}
		}
	}	
	post {
			always {
				script {
					def mailRecipients = "ashish.nargade@thermofisher.com ,Michael.Pu@thermofisher.com,amar.v@thermofisher.com"
					def jobName = currentBuild.fullDisplayName
					def mailFrom = "Jenkins"
					emailext mimeType: 'text/html',
					body: '''${SCRIPT, template="dtdm-email.template"}''',
					subject: "[Jenkins] ${jobName}",
					to: "${mailRecipients}",
					from: "${mailFrom}",
					replyTo: "${mailRecipients}",
					recipientProviders: [[$class: 'CulpritsRecipientProvider']]
				}
			}
	}
}
