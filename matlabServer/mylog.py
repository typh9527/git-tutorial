import time

def log(msg,taskid):
    msg = str(msg)
    date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print(date + ':' + taskid +':'+msg)

def error_log(taskid,error,error_type):
    date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print("%s:%s:%s" % (date ,error_type,error))
