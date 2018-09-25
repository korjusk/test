import subprocess

def create():
    bashCommand = 'touch delme.txt'
    output = subprocess.check_output(['bash','-c', bashCommand])
    output = subprocess.check_output(['bash','-c', 'ls'])
    return output

