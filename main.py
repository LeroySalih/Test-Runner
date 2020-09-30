from subprocess import run
import urllib.request
import hashlib 


result = run(["python", "test.py"], input=b'Salih\n12\n', capture_output=True)

print(str(result.stdout))
print("Test Passed!: ", hashlib.md5(result.stdout))

with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   




