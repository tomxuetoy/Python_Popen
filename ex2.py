import subprocess
p=subprocess.Popen('ls -al',shell=True,stdout=subprocess.PIPE)
for l in p.stdout:
    print l
