import subprocess
import os
import sendweb
'''
directorys即为数据库列表中的task
fileid，taskid为数据库列表中的id
'''
def unzip(directorys):
    '''解压文件'''
    directory,filename = os.path.split(directorys)
    work_path = os.path.abspath('.')
    #os.chdir(directory)
    #print(filename)
    print('unzip:'+work_path)
    print(directorys)
    print(directory)
    code = subprocess.call(["unzip",directorys,'-d',directory])
    if code == 0:
        print("unzip success")
    else:
        print("unzip failed")
        return False
    #: delete zip you have upzipped
    code = subprocess.call(['rm',directorys])
    #os.chdir(work_path)
    if code == 0:
        print("delete zip success!")
        return True
    else:
        print("delete zip failed!")
        return False

    
def zip(directorys,fileid):
    '''压缩文件，保存为fileid.zip'''
    directory,filename = os.path.split(directorys)
    fileid = directory + '/' + fileid
    filename,datatype = filename.split('.')
    #work_path = os.path.abspath('.')
    #os.chdir(directory)
    directorys = directory + '/' + filename[10:]
    zipfile = directory + '/' + filename[10:]
    code = subprocess.call(['zip','-r',fileid,zipfile])
    if code == 0:
        print("success zip")
        
    else:
        print("failed zip")
        return False
    print(zipfile) 
    #:delete file you have zipped
    code = subprocess.call(['rm','-r',zipfile])
    #os.chdir(work_path)
    if code == 0:
        print("delete file success!")
        return True
    else:
        print("delete file failed!")
        return False


def sendtoweb(directorys,taskid):
    '''移动文件到web服务器'''
    directory,filename = os.path.split(directorys)
    filename = directory+'/'+taskid + '.' + filename.split('.')[1]
    code = sendweb.sendtoweb('112.74.171.161',filename) 
    if code:
        print("Upload web success!")
    else:
        print("Upload web failed!")
        return False
    #:删除文件
    code = subprocess.call(['rm',filename])
    if code == 0:
        print('delete zip success!')
        return True
    else:
        print("delete zip failed!")
        return False

if __name__ == '__main__':
    #zip('workpath/joliu@s-an.org/1484748894test2.zip','70')
    print(sendtoweb('workpath/joliu@s-an.org/1484740759te.zip','74'))
