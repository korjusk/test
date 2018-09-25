import subprocess

def ls():
    bashCommand = 'ls'
    output = subprocess.check_output(['bash','-c', bashCommand])
    return output
