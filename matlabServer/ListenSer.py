import MySQLdb
import task
import ziptask
import time
import smtplib_build
class ListenSer():
    '''listen the task from mysqldb'''
    
    def __init__(self, number):
       #:the parallel number
        self.number = number;
    
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
            
    def gettask(self):
        try:
            task_list = []
            conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='WyrXa9')
            cur = conn.cursor()
            conn.select_db('task_db')
            sql = 'select * from task_list where status = 0 limit '+str(self.number)
            cur.execute(sql)
            ret = cur.fetchall()
            for sample in ret:
                #:do something here
                task_list.append([sample[0],sample[2],sample[1]])
            cur.close()
            conn.close()
            return task_list
        except MySQLdb as e:
            print("Mysql Error%d:%s" % (e.args[0], e.args[1]))

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
            
if __name__ == '__main__':
    test = ListenSer(2)
    i=test.checktask() 
    print(i)  
    while True:
        if test.checktask():

           lists = test.gettask()
           for li in lists:
               if ziptask.unzip(li[1]):
                   task.exectask(li[0])
               else:
                   test.failtask(str(li[0]),li[2])
                   print(str(li[0])+' :unzip failed')
                   continue
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
               else:
                   print(str(li[0])+' :zip failed!')
                   test.failtask(str(li[0]))    
        else:
            time.sleep(6)
            print(time.asctime()+": sleep")
   
