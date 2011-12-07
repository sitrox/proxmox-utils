import logging
import subprocess

class ShellUtils(object):
  @classmethod
  def configure_logging(cls):
    logging.basicConfig(level=logging.INFO,
      format='%(asctime)s %(levelname)s %(message)s')

  @classmethod
  def command(cls, command, expected_retvals=[0], wait=True, shell=False):
    if isinstance(command, basestring):
      raise Exception("String commands are not supported.")
    process = subprocess.Popen(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if not wait:
      return
    lines = process.stdout.readlines()
    retval = process.wait()
    res = ''.join(lines).lstrip().rstrip()
    if not retval in expected_retvals:
      raise Exception('The command "' + ' '.join(command) + '" could not be executed.')
    return res
  
  @classmethod
  def confirm_continue(cls, prompt="Do you want to continue?", resp=False, exit_code=0):
    if not cls.confirm(prompt, resp):
      exit(exit_code)
  
  def cp(cls, file_from, file_to, recursive=False):
    command = ['cp']
    
    if recursive:
      command.push('-r')
    
    command += [file_from, file_to]
    print command
    #ShellUtils.command(command)
  
  @classmethod
  def confirm(cls, prompt=None, resp=False):
    """
    http://code.activestate.com/recipes/541096/
    prompts for yes or no response from the user. Returns True for yes and
    False for no.
    
    'resp' should be set to the default value assumed by the caller when
    user simply types ENTER.
    
    >>> confirm(prompt='Create Directory?', resp=True)
    Create Directory? [y]|n: 
    True
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: 
    False
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: y
    True
    
    """
    
    if prompt is None:
      prompt = 'Confirm'
    
    if resp:
      prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
      prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
    
    while True:
      ans = raw_input(prompt)
      if not ans:
        return resp
      if ans not in ['y', 'Y', 'n', 'N']:
        print 'please enter y or n.'
        continue
      if ans == 'y' or ans == 'Y':
        return True
      if ans == 'n' or ans == 'N':
        return False