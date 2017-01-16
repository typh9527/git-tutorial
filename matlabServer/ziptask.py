import os
import subprocess

def unzip(directorys):
    directory,filename = os.path.split(directorys)
    work_path = os.path.abspath('.')
    os.chdir(directory)
    print(filename)
    code = subprocess.call(["unzip",filename])
    if code == 0:
        print("unzip success")
    else:
        print("unzip failed")
    #: delete zip you have upzipped
    code = subprocess.call(['rm',filename])
    if code == 0:
        print("delete zip success!")
    else:
        print("delete zip failed!")
    
    os.chdir(work_path)
    
def zip(directorys,fileid):
    directory,filename = os.path.split(directorys)
    filename,datatype = filename.split('.')
    work_path = os.path.abspath('.')
    os.chdir(directory)
    zipfile = filename[10:]
    code = subprocess.call(['zip','-r',fileid,zipfile])
    if code == 0:
        print("success zip")
    else:
        print("failed zip")
    
    #:delete file you have zipped
    code = subprocess.call(['rm','-r',zipfile])
    if code == 0:
        print("delete file success!")
    else:
        print("delete file failed!")
    os.chdir(work_path)

def sendtoweb(directorys,taskid):
    directory,filename = os.path.split(directorys)
    work_path = os.path.abspath('.')
    os.chdir(directory)
    filename = taskid + '.' + filename.split('.')[1]
    code = subprocess.call(['mv',filename,'/var/www/html/'])
    if code == 0:
        print("Upload web success!")
    else:
        print("Upload web failed!")

if __name__ == "__main__":
    #unzip('workpath/joliu@s-an.org/1484575120test2.zip') 
    #zip('workpath/joliu@s-an.org/1234567890test2.zip','22')
    sendtoweb('workpath/joliu@s-an.org/1234567890test2.zip','22')
