import re
import os
import sys
import subprocess

info = os.path.abspath(sys.argv[0]).split('\\')
disk_name, file_name = info[0], info[-1]
tmp = subprocess.check_output('mountvol ' + disk_name + ' /L').decode()
id1 = re.sub(r'[\\?{}]', '', tmp.replace('Volume', '').lstrip())
id2 = ''

print(id1, id2, sep='\n')

var = input()
with open(file_name, 'r') as rf:
	txt = rf.read().split('\n')

if var == '0':
	print('Success') if id1 == id2 else print('Fail')
else:
	print(txt[9])
	with open(file_name, 'w') as wf:
