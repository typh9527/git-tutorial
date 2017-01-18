import MySQLdb
import task
import ziptask
import time
import smtplib_build
class ListenSer():
    '''处理队列中的任务类'''
    
    def __init__(self,number):
        #:the parallel number
        self.number = number  
    def checktask(self):
        try:
            conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='WyrXa9')
            cur = conn.cursor()
            conn.select_db('task_db')
            cur.execute("select count(*) from task_list where status = 0")
            result = cur.fetchone()
            cur.close()
            conn.close()
            if result[0] == 0:
                return False
            else:
                return True
        except MySQLdb as e:
            print("Mysql Error:%d:%s" % (e.args[0], e.args[1]))
            
    #def gettask(self):
    #    try:
    #        task_list = []
    #        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='WyrXa9')
    #        cur = conn.cursor()
    #        conn.select_db('task_db')
    #        sql = 'select * from task_list where status = 0 limit 1'
    #        cur.execute(sql)
    #        ret = cur.fetchall()
    #        for sample in ret:
    #            #:返回一个二维数组
    #            task_list.append([sample[0],sample[2],sample[1]])
    #        cur.close()
    #        conn.close()
    #        return task_list
    #    except MySQLdb as e:
    #        print("Mysql Error%d:%s" % (e.args[0], e.args[1]))

    def failtask(self,taskid,to_email):
        try:
            conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='WyrXa9')
            cur = conn.cursor()
            conn.select_db('task_db')
            sql = 'update task_list set status = 2 where id = '+taskid
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            #: 发送邮件通知任务失败
            subject = "进度详情"
            body_text = "任务失败\n请联系管理员,修改任务"
            smtplib_build.send_email(subject,body_text,to_email)
        except MySQLdb as e:
            print("MySQL Error%d:%s" % (e.args[0],e.args[1]))

def gettask(number):
    '''获取队列中的任务，返回队列列表'''
    try:
        task_list = []
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='WyrXa9')
        cur = conn.cursor()
        conn.select_db('task_db')
        #:修改此处的4来修改每次从列表中提取任务数
        sql = 'select * from task_list where status = 0 limit 4'
        cur.execute(sql)
        ret = cur.fetchall()
        for sample in ret:
            #:返回队列列表的顺序，id，task，user_email
            task_list.append([sample[0],sample[2],sample[1]])
            sql = 'update task_list set status = 1 where id = '+str(sample[0])
            cur.execute(sql)
            conn.commit()
        cur.close()
        conn.close()
        return task_list
    except MySQLdb as e:
        print("Mysql Error%d:%s" % (e.args[0], e.args[1]))

def run_listen(li):
    '''顺序实现一个完整的matlabserver的过程'''
    test = ListenSer(1)
    if ziptask.unzip(li[1]):
        task.exectask(li[0])
    else:
        test.failtask(str(li[0]),li[2])
        print(str(li[0])+' :unzip failed')
        return False
    if ziptask.zip(li[1],str(li[0])):
        if ziptask.sendtoweb(li[1],str(li[0])):
            print(str(li[0])+' : success!')
            subject = "进度详情"
            body_text = r'任务成功\n结果下载地址<a href="http://192.168.1.102'+str(li[0])+r'.zip">link</a>'
            to_email = li[2]
            smtplib_build.send_email(subject,body_text,to_email)
        else:
            print(str(li[0])+' :sendtoweb failed!')
            test.failtask(str(li[0]),li[2])
            return False
    else:
        print(str(li[0])+' :zip failed!')
        test.failtask(str(li[0]))
        return False
 
if __name__ == "__main__":
    lists = gettask(0)
    print(lists)
    for li in lists:
        print(li[0])
        run_listen(li) 
