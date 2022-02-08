import subprocess
import time

print('Installing Dependencies ...')
print()

time.sleep(1.5)

subprocess.call('pip install --upgrade pip')
subprocess.call('pip install requests')
subprocess.call('pip install --upgrade requests')
subprocess.call('pip install PyQt5')
subprocess.call('pip install --upgrade PyQt5')

time.sleep(1.5)

print()
print('Dependencies Installed !')