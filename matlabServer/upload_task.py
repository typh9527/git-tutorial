import MySQLdb
import time

def save_task(user_email,filename):
    '''保存任务到服务器'''
    start_time = time.asctime()
    task=filename
    value = [user_email,task,start_time]
    try:
        conn = MySQLdb.connect(host='192.168.1.102',user='root',passwd='WyrXa9')
        cur = conn.cursor()
        conn.select_db('task_db')
        cur.execute("insert into task_list(user_email,task,start_time) values (%s,%s,%s)",value)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb as e:
        print("Mysql Error%d:%s" % (e.args[0],e.args[1]))


if __name__ == '__main__':
    user_email = 'joliu@s-an.org'
    task = 'out.py'
    save_task(user_email,task)
