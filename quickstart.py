from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
# To list all files in your google drive at the root folder
file_list1 = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# To list asll files in a particular folder. (***)
#file_list1 = drive.ListFile({'q': "'{ID of the file}' in parents and trashed=false"}).GetList()

for file1 in file_list1:
   print('title: %s, id: %s' % (file1['title'], file1['id']))
   #file1.GetContentFile(file1['title'])


