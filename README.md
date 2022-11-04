# area52
Simple tool to configure servers using python backend

## How it works:

This repository consists of all the code needed to create a pypi/pip package that contains a command line based tool to configure the server. The tool takes server configuration definition as input and runs through the definition in a predefined order in a given server to setup specific softwares and configuration.

The tool exposes a command line binary (I named it as area52 :)) that takes subcommand parsesteps and start looking for files with extension ".hc". The first file it loads is "runlist.hc" which defines the order of execution

'''
{
  "run_list": [
  "recipe[provision_dirs]",
  "recipe[install_apt_packages]",
  "recipe[start_service]"
  ]
}
'''
Each entry in the recipe indicates that there exists another file with that name in the same directory (e.g provision_dirs.hc) and in which order the tool shall execute them.

Each recipe file consists of action which instruct what needs to be installed or configured. For example "install_apt_packages.hc" defines what apt packages to be installed in ubuntu or debian OS

'''
package "systemctl" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "systemctl"
}

package "apache2" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "apache2"
}

package "php7.2" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "php7.2"
}

package "libapache2-mod-php7.2" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "libapache2-mod-php7.2"
}

package "python3" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "python3"
}
'''

Each action has a corresponding processor class in the actions directory

project_root
|
|...plugins
    |
    |...actions
        |directory.py
        |file.py
        |package.py
        |service.py
        |shell.py
        |template.py

There is also a set  of helper classes that helps in iterating over all the *.hc files and creating a queue for processing the tasks in the defeind order as below

project_root
|
|...plugins
    |
    |...helper
        |queuesteps.py

'''
task_order = [
              "file", 
              "directory",
              "template", 
              "package", 
              "service"]
'''
## Features 

	• Tool is built as a python package which could be installed using setup.py or pip. 
Use hcl language formatted task definition. Pyhcl is used to parse the hcl dsl
	• Actions are added to the package as plugins. Every supported action has a corresponding class in "plugins/action" directory with the exact same file name. Each such file shall implement method "process(self, action_data_obj)".
	• This enables building new feature easy as new action can be added easily with a new module file in the "plugins/actions" dir.
	• Docker is used to test the tool in isolation and the relevant dockerfile is added

## What could be improved
  • Authentication and authorization module
	• Automatically detect OS version and route to corresponding class
	• Properly articulated task prioritization and chaining mechanism
	• Maintaining some kind of state within a .hcstate directory or similar.
  • Implementing template binding with Jinja2 module (started that work but could not finish it )


## Local Installation:

| Step#         |   Details     |
| ------------- |:--------------|
|Step1:| git clone <repo>/area52.git |
|Step2:| cd area52|
|Step3:| virtualenv venv|
|Step4:| source venv/bin/activate|
|Step5:| pip install -r requirements.txt|
|Step6:| ./clean_workspace|

This shall generate a package under project_root --> plugins --> package --> plugins-1.1.tar.gz. The setup.py includes all dependencies for this work in Ubuntu or Debian OS. 

## Configure remote host steps

| Step#         |   Details     |
| ------------- |:--------------|
|Step1:| Create a repo with all *.hc files, template files (e.g index.html, info.php), the python package plugins-1.1.tar.gz |
|Step2:| Use scp to copy the files in a directory on the remote host scp -pr area52impl/ root@<host_ip>:/root/area52impl|
|Step3:| Check python and pip is already installed if not run the following|
|Step4:| Run ./configure.sh or the bash script inside this file|
|Step5:| Run pip3 install -r requirements.txt >> plugins-1.1.tar.gz to install the tool |
|Step6:| Run area52 parsesteps --template_path="files.hc" to start configuration|
|Step7:| Open a browser and enter http://<host_public_ip>/info.php to load the website|




## Usage:

### to find available commands run 
area52 --help

### To initiate the host configuration sequence. One can ommit --template_path param
area52 parsesteps --template_path="files.hc



