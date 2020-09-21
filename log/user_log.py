import logging,os,datetime

class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d" + ".log")
        log_name = log_dir + '\\' +  log_file
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s ----> %(funcName)s %(levelno)s %(levelname)s----> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        #self.logger.debug("test123")


    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    obj = UserLog()
    log = obj.get_log()
    log.debug("这个才是真log")
    obj.close_handle()
