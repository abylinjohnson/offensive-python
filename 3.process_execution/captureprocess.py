#Capturing process execution

import subprocess

#Executes "ls -la" and capture output
proc = subprocess.Popen("ls -la",shell=True,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        stdin=subprocess.PIPE)
#waits until it finishes
exit_code = proc.wait()

#reads output
results = proc.stdout.read()
print(results)


