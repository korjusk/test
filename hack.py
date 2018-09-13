import subprocess

bashCommand = "sudo locate -i paroolid.json"
output = subprocess.check_output(['bash','-c', bashCommand])

print output
