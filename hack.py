import subprocess

bashCommand = "cat test_dynamodb.py"
output = subprocess.check_output(['bash','-c', bashCommand])

print output
