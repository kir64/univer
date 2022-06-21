import os


print('Enter 0 to calculate hash, 1 to check hashes.')
mod = input()
print('Enter the path.')
path = input()

if mod != '0' and mod != '1':
	print('Wrond input!')
else:
	if os.path.exists(path):
		if mod == '0':
				check_table = {}
				hash_table = dict()
				files_lst = os.listdir(path)

				for i in files_lst:
					file_path = path + '\\' + i

					with open(file_path, 'rb') as txt:
						sum, chunk = 0, txt.read(4)
						while chunk:
							sum ^= int.from_bytes(chunk, "little", signed=True)
							chunk = txt.read(4)
					check_table[i] = sum

					with open('output.txt', 'w') as wf:
						for k, v in check_table.items():
							print(f"{k} {v}", file=wf)
		else:
			check_table, current = {}, {}
			with open('output.txt', 'r') as rf:
				s = rf.readline().split()
				while s:
					check_table[s[0]] = s[1:]
					s = rf.readline().split()
			files_lst = os.listdir(path)

			for i in files_lst:
				file_path = path + '\\' + i
				with open(file_path, 'rb') as txt:
					sum, chunk = 0, txt.read(4)
					while chunk:
						sum ^= int.from_bytes(chunk, "little", signed=True)
						chunk = txt.read(4)
				current[i] = sum


			flag = True
			if set(check_table.keys()) ^ set(files_lst) != set():
				flag = False
	
			if flag:
				for k, v in current.items():
					if check_table[k][0] != str(v):
						flag = False
						break
			if flag:
				print('Equal hashes.')
			else:
				print('Hashes differ.')

			
	else:
		print('Wrond input!')
