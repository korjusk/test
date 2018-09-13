import subprocess

bashCommand = "ls -R"
output = subprocess.check_output(['bash','-c', bashCommand])

print output
