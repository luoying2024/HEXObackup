import os
m = r'D:\Deskbackup.txt'
if not os.path.exists(m):
  os.mkdir(m)
os.system(m)

# pyinstaller set.py