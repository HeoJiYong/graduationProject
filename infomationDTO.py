'''
0 uesrinfo
1 gps
2 alarm
3 mood

4 uv
5 humidity
6 tempterature

class 하나 만들고 관리 (파일대신)
'''
import infomationDAO
from howowConfig import *
class infomationDTO():
    def __init__(self):
        self.dao = infomationDAO.infomationDAO(host,user,password,db,charset,port)
        '''
        self.command = ['userinfo','gps','alarm','mood','uv','temperature','humidity']
        self.infomations = {'userinfo':'','gps':'','alarm':'','mood':'',
                      'uv':'','temperature':'','humidity':''}
        '''

        self.userinfo = 'NoUserInfo'
        self.gps = 'NoLocation'
        self.alarm = 'NoAlarm'
        self.mood = 0

        self.uv = 0
        self.temperature = 0.0
        self.humidity = 0.0
        pass

    def setUserinfo(self, userinfo):
        self.userinfo = userinfo

    def setGps(self, gps):
        self.gps = gps

    def setAlarm(self, alarm):
        self.alarm = alarm

    def setMood(self, mood):
        self.mood = mood

    def setUv(self, uv):
        self.uv = uv

    def setTemperature(self, temperature):
        self.temperature = temperature

    def setHumidity(self, humidity):
        self.humidity = humidity

    #-------------------

    def getUserinfo(self):
        return self.useinfo

    def getGps(self):
        return self.gps

    def getAlarm(self):
        return self.alarm

    def getMood(self):
        return self.mood

    def getUv(self):
        return self.uv

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def update(self):
        #print(self.uv,type(self.uv))
        #print(self.humidity,type(self.humidity))
        #print(self.temperature,type(self.temperature))
        self.dao.update(uv=str(self.uv),humidity=str(self.humidity),temperature=str(self.temperature))

    def select(self):
        rows = self.dao.select()
        self.userinfo = rows[0]
        self.gps = rows[1]
        self.alarm = rows[2]
        self.mood = rows[3]
        self.uv = rows[4]
        self.humidity = rows[5]
        self.temperature = rows[6]

    def getDatas(self):
        return self.userinfo,self.gps,self.alarm,self.mood,self.uv,self.humidity,self.temperature
    '''
    def getInfomations(self):
        #import DAO,
        #DAO 생성
        #data return
        pass

    def setInfomations(self):
        self.dao
    '''
    def __del__(self):
        pass


def main1():
    testDTO = infomationDTO()
    gpss=['청주','서울','서천','화성','부산']
    import time
    import random
    while True:
        testDTO.setUserinfo('test'+str(random.randrange(1,10)))
        testDTO.setGps(gpss[random.randrange(0,5)])
        testDTO.setAlarm(str(random.randrange(2000,2021))+'-'+str(random.randrange(1,13))+'-'+str(random.randrange(1,30)) + '-' + str(random.randrange(0,24))+str(random.randrange(0,60)))
        testDTO.setMood(random.randrange(0,8))
        testDTO.setUv(random.randrange(0,2))
        testDTO.setHumidity(random.randrange(10,55))
        testDTO.setTemperature(random.randrange(0,36))
        testDTO.update()
        testDTO.select()
        testDTO.getDatas()
        time.sleep(2)
        pass
    pass

def main():
    testDTO = infomationDTO()
    import time
    while True:
        testDTO.select()
        print(testDTO.getDatas())
        print(testDTO.getAlarm()[-4:])
        alarmFromDTO = testDTO.getAlarm()[-4:] #연, 월, 일, 시각 에서 시각만 가져온다.(ex. 2030)
        alarmHour = str(alarmFromDTO[:2])
        alarmMinute= str(alarmFromDTO[2:])
        print(alarmHour,alarmMinute)
        print(testDTO.getMood())
        time.sleep(2)

    pass
if __name__ == "__main__":
    main()
    pass