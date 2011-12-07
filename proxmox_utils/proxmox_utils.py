import os
from shell_utils import ShellUtils

class KVMUtils(object):
  REGEX_TEMPLATE_NAME = '^[a-zA-Z0-9_-]+$'
  
  @classmethod
  def config_path(cls, vm_id):
    return "/etc/qemu-server/%s.conf" % vm_id
    
  @classmethod
  def image_path(cls, vm_id):
    return "/var/lib/vz/images/%s" % vm_id
  
  @classmethod
  def tpl_config_path(cls, template_name):
    return KVMUtils.config_path("t_%s" % template_name)

  @classmethod
  def tpl_image_path(cls, template_name):
    return KVMUtils.image_path("t_%s" % template_name)
  
  @classmethod
  def exists(cls, vm_id):
    return os.path.exists(KVMUtils.config_path(vm_id)) or os.path.exists(KVMUtils.image_path(vm_id))
  
  @classmethod
  def tpl_exists(cls, template_name):
    return KVMUtils.exists("t_%s" % template_name)
    
  @classmethod
  def status(cls, vm_id):
    return ShellUtils.command(["qm", "status", vm_id])
    
  @classmethod
  def suspend(cls, vm_id):
    ShellUtils.command(["qm", "suspend", vm_id])
  
  @classmethod
  def resume(cls, vm_id):
    ShellUtils.command(["qm", "resume", vm_id])
    
  @classmethod
  def stop(cls, vm_id):
    ShellUtils.command(["qm", "stop", vm_id])