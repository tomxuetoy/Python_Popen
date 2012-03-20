import subprocess
 
f = open('out.txt', 'w')
subprocess.Popen('ls', stdout=f)
