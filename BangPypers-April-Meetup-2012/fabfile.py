
from fabric.api import *
from fabric.contrib import *
import boto

env.hosts = [ '46.137.214.33' ]
env.key_filename = [ '/home/deepak/.ssh/deepak-key-pair.pem' ]
env.user = 'ubuntu'

def init():
    provision_vm()
    install_baseline()
    install_py()
    install_django()
    
def provision_vm():
    pass
    
def install_baseline():
    sudo('apt-get update')
    sudo('apt-get -y upgrade')
    sudo('apt-get -y install vim', shell=False)
    sudo('apt-get -y install build-essential', shell=False)
    sudo('apt-get -y install git-core subversion mercurial', shell=False)
    
def install_py():
    sudo('apt-get -y install python-imaging python-openssl', shell=False)
    sudo('apt-get -y install python-setuptools python-dev', shell=False)
    sudo('apt-get -y install python-pip libpq-dev', shell=False)
    sudo('apt-get -y install python-mysqldb sqlite3', shell=False)
    sudo('apt-get -y install python-django', shell=False)
    sudo('DEBIAN_FRONTEND=noninteractive apt-get -y install postfix', shell=False)
    sudo('gem install haml', shell=False)
    sudo('pip install virtualenv', shell=False)
    sudo('pip install fabric', shell=False)
    print "Setup completed!"
    
def install_django():


