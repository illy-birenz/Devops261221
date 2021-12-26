properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("close"){
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/illy-birenz/Devops261221.git']]])
    }
    stage("show files")
    bat "dir"
}
