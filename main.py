#Filename:backup.py
import os,time,zipfile
#要备份的文件的列表
# source = ['D:\\SAKURAblog']#构造好备份目标文件
import os
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')
sou = 'D:\\Deskbackup.txt'
if not os.path.exists(sou):
  print('NO SUCH FILE')
else:
  with open(sou) as f:
      content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
      source = [x.strip() for x in content]
  print(source)
  target_dir = 'D:\\Backup'

  # 使用zipfile来压缩#创建压缩包变量z
  for back_dir in source:

      print('Start PACKing..'+back_dir)
      # creat folder name
      end = '_'+os.path.basename(os.path.normpath(back_dir)) # endding name
      timekey = os.sep + time.strftime('%Y%m%d%H%M')
      today = target_dir + timekey + end

      # creat file name
      if not os.path.exists(today):
          os.mkdir(today)
          # cancel the note function
          comment = ''
          #    input("typeing..：")
          if len(comment) == 0:
              target = today + os.sep + time.strftime('%Y%m%d%H%M')
          else:
              target = today + os.sep + time.strftime('%Y%m%d%H%M') + comment.replace(' ', '_')

      z = zipfile.ZipFile(target + end + '.zip', 'w')

      # comming soon
      for root, filedirs, files, in os.walk(back_dir):
          # print('PACKing..',root)
          for file in files:
              z.write(os.path.join(root, file))
      z.close()
      print(back_dir + ' 成功备份至', target)





# pyinstaller -F --path=src mains.py
# pyinstaller  main.py
