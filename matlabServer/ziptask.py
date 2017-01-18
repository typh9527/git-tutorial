import os
import subprocess

def unzip(directorys):
    directory,filename = os.path.split(directorys)
    work_path = os.path.abspath('.')
    os.chdir(directory)
    print(filename)
    print('unzip:'+work_path)
    code = subprocess.call(["unzip",filename])
    if code == 0:
        print("unzip success")
    else:
        print("unzip failed")
        return False
    #: delete zip you have upzipped
    code = subprocess.call(['rm',filename])
    os.chdir(work_path)
    if code == 0:
        print("delete zip success!")
        return True
    else:
        print("delete zip failed!")
        return False

    
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
        return False
    
    #:delete file you have zipped
    code = subprocess.call(['rm','-r',zipfile])
    os.chdir(work_path)
    if code == 0:
        print("delete file success!")
        return True
    else:
        print("delete file failed!")
        return False


def sendtoweb(directorys,taskid):
    directory,filename = os.path.split(directorys)
    work_path = os.path.abspath('.')
    os.chdir(directory)
    filename = taskid + '.' + filename.split('.')[1]
    code = subprocess.call(['mv',filename,'/var/www/html/'])

    os.chdir(work_path)
    if code == 0:
        print("Upload web success!")
        return True
    else:
        print("Upload web failed!")
        return False

