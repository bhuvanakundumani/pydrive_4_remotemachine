from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
# To list all files in your google drive at the root folder
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# to list all files in the google drive root
for file in file_list:
   print('title: %s, id: %s' % (file['title'], file['id']))
# If you want to download a specfic file, you can get the id of the file in the drive using the code in line 10 -11 . Once u have got the id of the file, you can 
# To list all files in a particular folder. (***)
file1 = drive.ListFile({'q': "'{ID of the file}' in parents and trashed=false"}).GetList()

# to download all files in a folder . Here file1 is the folder that we want to download
for file in file1:
   print('title: %s, id: %s' % (file['title'], file['id']))
   file1.GetContentFile(file1['title'])


# if you want to specifically download a single file . Get the file id using the code in lines 10 -11
fileID = '<enter the file id here>'
filetodownload = drive.CreateFile({'id':fileID})
filetodownload.GetContentFile('<enter the name that u want to use for the downloaded file here>')
print("done")


