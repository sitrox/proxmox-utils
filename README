=============
Proxmox utils
=============

Installation
============
Install setuptools

  aptitude install python-setuptools
  
Get source

  git://github.com/remofritzsche/proxmox-utils.git
  
Install

  cd proxmox-utils
  python setup.py build
  sudo python setup.py install

Usage
=====

  ./kvm-clone <from-id> <to-id>
  
    This clones a KVM machine (NOTE: not a template) from one id to the other. If the source
    machine is currently running, the script will automatically suspend it and resume it again
    after the machine has been copied. To the end of the script, it gives you the possibility to
    edit the configuration file for the target machine. In any case, this has to be done in order
    to adapt the image paths contained in the configuration files.
  
  ./kvm-remove <machine-id>
  
    This fully removes a KVM machine and it's configuration. You can also delete such a machine
    directly via the Proxmox Web Interface, however a few files will be left out by Proxmox.
  
  ./kvm-create-template <machine-id> <template-name>
    
    Creates a new template from an installed KVM machine with <machine-id>. Make sure to
    edit the generated template configuration file (especially name, comment and image file
    location).
  
  ./kvm-list-templates
  
    Lists the available template names.
  
  ./kvm-activate-template <template-name> <to-id>
  
    This copies over an existing template to a machine of a certain ID.