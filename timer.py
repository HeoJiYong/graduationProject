'''
yead, month, day, hour, minute, second, microsecond
'''
import datetime

class timer:
    def __init__(self):
        #self.year = 1900
        #self.month = -1
        #self.day = -1
        self.hour = -1
        self.minute = -1
        self.updateNow()
        pass

    def updateNow(self):
        value = datetime.datetime.now()
        #self.year = value.year
        #self.month = value.month
        #self.day = value.day
        self.hour = value.hour
        self.minute = value.minute
        if self.hour < 10:
            self.hour="0"+str(self.hour)
        if self.minute < 10:
            self.minute = "0"+str(self.minute)
        self.hour = str(self.hour)
        self.minute = str(self.minute)
        pass

    def getNow(self):
        return self.hour, self.minute
        pass

def main():
    import time
    testTimer = timer()
    presentHour,presentMinute = 0,0
    while True:
        testTimer.updateNow()
        h,m=testTimer.getNow()
        if presentMinute != m:
            print(h+'시 '+m+'분 입니다')
            presentHour,presentMinute =h,m
        time.sleep(1)
        pass
    pass

if __name__ == "__main__":
    main()
    pass