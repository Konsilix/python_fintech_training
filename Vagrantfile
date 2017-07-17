# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 4
  end
  config.vm.box = "ubuntu/xenial64"
    # Prevent TTY Errors (copied from laravel/homestead: "homestead.rb" file)... By default this is "bash -l".
    config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
    config.vm.provision :shell, path: "./setup/bootstrap.sh"
    config.vm.provision "file", source: "./setup/.vimrc", destination: "~/.vimrc"
    config.vm.provision "file", source: "./setup/requirements.txt", destination: "~/dev/python"
    config.vm.provision "file", source: "./setup/test_python_env.py", destination: "~/dev/python"
end

