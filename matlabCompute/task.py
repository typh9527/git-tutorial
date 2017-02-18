import MySQLdb
import time
import os
import subprocess
def exectask(id):
    '''执行matlab程序'''
    conn = MySQLdb.connect(host='112.74.171.161', user='root', passwd='WyrXa9')
    cur = conn.cursor()
    conn.select_db('task_db')
    sql = 'update task_list set status = 1 where id = '+str(id)
    cur.execute(sql)
    conn.commit()
    sql = 'select * from task_list where id='+str(id)
    cur.execute(sql)
    result = cur.fetchone()
    #:此处要求压缩包内的文件夹必须和上传的压缩包文件名一致
    file_directory = result[2]
    directory,filename = os.path.split(file_directory)
    filename = filename.split('.')[0][10:]
    directory = os.path.join(directory,filename)
    work_path = os.path.abspath('.')
    print(work_path)
    #os.chdir(directory)
    code = subprocess.call(['matlab','-nodesktop','-nosplash','-nojvm',r"-r 'cd "+directory+";main;quit'"])
    if code == 0:
        print("run success!")
    else:
        print("run failed!")
    #os.chdir(work_path)
    sql = 'update task_list set end_time = "'+time.asctime()+'" where id = '+str(id)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    exectask(50)
    
