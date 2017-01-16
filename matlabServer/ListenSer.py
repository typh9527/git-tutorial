import MySQLdb
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
            i=cur.execute("select count(*) from task_list where status = 0")
            cur.close()
            conn.close()
            return i
        except MySQLdb as e:
            print("Mysql Error:%d:%s" % (e.args[0], e.args[1]))
            
    def gettask(self):
        try:
            conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='WyrXa9')
            cur = conn.cursor()
            conn.select_db('task_db')
            sql = 'select * from task_list where status = 0 limit '+str(self.number)
            cur.execute(sql)
            ret = cur.fetchall()
            for sample in ret:
                sql='update task_list set status = 1 where id = '+str(sample[0])
                cur.execute(sql)
                conn.commit()
                print(sample[0])
            cur.close()
            conn.close()
        except MySQLdb as e:
            print("Mysql Error%d:%s" % (e.args[0], e.args[1]))
            
if __name__ == '__main__':
    test = ListenSer(2)
    i=test.checktask() 
    print(i)   
    test.gettask()
