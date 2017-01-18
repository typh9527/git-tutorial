import MySQLdb
import time
import os
import subprocess
def exectask(id):
    '''run the task!'''
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='WyrXa9')
    cur = conn.cursor()
    conn.select_db('task_db')
    sql = 'update task_list set status = 1 where id = '+str(id)
    cur.execute(sql)
    conn.commit()
    sql = 'select * from task_list where id='+str(id)
    cur.execute(sql)
    result = cur.fetchone()
    #:do something here
    file_directory = result[2]
    directory,filename = os.path.split(file_directory)
    filename = filename.split('.')[0][10:]
    directory = os.path.join(directory,filename)
    work_path = os.path.abspath('.')
    print(work_path)
    os.chdir(directory)
    code = subprocess.call(['matlab','-nodesktop','-nosplash','-nojvm',r"-r 'main;quit'"])
    if code == 0:
        print("run success!")
    else:
        print("run failed!")
    os.chdir(work_path)
    sql = 'update task_list set end_time = "'+time.asctime()+'" where id = '+str(id)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    exectask(23)
    
