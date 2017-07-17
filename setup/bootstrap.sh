#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get upgrade --assume-yes --fix-missing
apt-get install vim wget git zlib1g-dev --assume-yes
apt-get install python-pip --assume-yes --fix-missing
apt-get install unixodbc unixodbc-dev freetds-dev tdsodbc

export RUN_USER="ubuntu"
export RUNUSER_PROG="/sbin/runuser"

export COMMAND=$(cat <<-'HERE1a'
    echo "\"echo \"in .profile\" >> $HOME/.profile\""
    echo "\"echo \"in .bashrc\" >> $HOME/.bashrc\""
    mkdir -p ~/dev/python
    sudo -H pip install --upgrade pip
    sudo -H pip install -r /vagrant/setup/requirements.txt
HERE1a
)

${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

