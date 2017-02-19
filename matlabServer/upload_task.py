import MySQLdb
import time
import mylog

def save_task(user_email,filename):
    '''保存数据到服务器'''
    start_time = time.asctime()
    task=filename
    value = [user_email,task,start_time]
    try:
        conn = MySQLdb.connect(host='112.74.171.161',user='root',passwd='WyrXa9')
        cur = conn.cursor()
        conn.select_db('task_db')
        cur.execute("insert into task_list(user_email,task,start_time) values (%s,%s,%s)",value)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb as e:
        mylog.log("MySql error","upload_task.save_task")
        print("Mysql Error%d:%s" % (e.args[0],e.args[1]))


if __name__ == '__main__':
    user_email = 'joliu@s-an.org'
    task = 'out.py'
    save_task(user_email,task)

