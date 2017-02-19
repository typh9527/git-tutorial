import ListenSer
import time

from threading import Thread

class RunThread(Thread):
    """
    多进程运行任务
    """
    
    def __init__(self,li):
        """初始化类"""
        Thread.__init__(self)
        self.list = li

    def run(self):
        ListenSer.run_listen(self.list)
        print(time.asctime)

if __name__ == '__main__':
    while True:
        #:输入每次循环从列表中取多少组任务
        lists = ListenSer.gettask(4)
        if len(lists) == 0:
            time.sleep(6)
        else:
            for li in lists:
                print(time.asctime())
                my_thread = RunThread(li)
                my_thread.start()
        
