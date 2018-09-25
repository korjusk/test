import subprocess

bashCommand = touch delme.txt
output = subprocess.check_output([bash,-c, bashCommand])

print output
