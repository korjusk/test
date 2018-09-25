import subprocess

def create():
    bashCommand = 'cat ~/.aws/credentials'
    output = subprocess.check_output(['bash','-c', bashCommand])
    return output

