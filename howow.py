'''
수정시간 : 2020-11-21-

To do

'''

'''기본제공 라이브러리'''
import threading
import time

'''사용자정의 라이브러리'''
import howowConfig      #config 파일
import sensorDHT        #온습도 센서
import sensorUV         #자외선 센서
import moodLED          #무드등
import timer            #현재시간 알기위해(알람기능에서)
import infomationDTO    #DB업뎃용 (여기서 DAO import함)
import flowerState

'''객체 정의'''
DHT = sensorDHT.DHTSensor(howowConfig.dhtPin)
UV = sensorUV.UVSensor(howowConfig.uvPin)
LED = moodLED.LED(howowConfig.ledPin,howowConfig.ledNum)
Timer = timer.timer()
DTO = infomationDTO.infomationDTO()
Flower=flowerState.flowerState()

'''스레드 함수 정의'''
#센서값(온도 습도 UV), 시간 업데이트
def sensors(snesorCycle):
    while True:
        DHT.updateData()
        UV.updateData()
        Timer.updateNow()
        Flower.updateFlowerState(DHT.temperature,DHT.humidity,UV.UV)

        time.sleep(snesorCycle)  # Cycle 주기마다 업데이트

#알람 시간에 맞춰 led 킨다
def led(ledCycle):
    # (DTO에서 가져온 시간) [비교] (Timer 에서 가져온 시간)
    while True:
        alarmFromDTO = DTO.getAlarm()[-4:] #연, 월, 일, 시,분 에서 시,분 만 가져온다.(ex. 2030)
        alarmHour = alarmFromDTO[:2]    #알람 시 만 추출
        alarmMinute= alarmFromDTO[2:]   #알람 분 만 추출
        hour,minute = Timer.getNow()    #현재 시,분
        if hour == alarmHour and minute == alarmMinute:
            LED.updateColor(DTO.getMood())  #색깔 업데이트 후
            LED.ledOn() #led on
        else:
            LED.ledOff()
        time.sleep(ledCycle)
    pass

#DB에서 받아오는 함수
def receiver(Cycle):
    while True:
        #DTO에 저장
        DTO.setUv(UV.UV)
        DTO.setHumidity(DHT.humidity)
        DTO.setTemperature(DHT.temperature)
        DTO.setFlower(Flower.getFlowerState())
        DTO.update()  # DB에 센서값 저장

        time.sleep(Cycle)
        DTO.select() #DB에서 모든값 가져오기
        print("DTO- select : ",DTO.getDatas())
        time.sleep(Cycle)
    pass

#DB로 주는 함수
def sender(Cycle):
    while True:

        time.sleep(Cycle)
    pass


'''메인 함수'''
def main():
    theadSensor = threading.Thread(target = sensors,args=[howowConfig.sensorCycle])
    threadLED = threading.Thread(target=led,args=[howowConfig.ledCycle])
    threadReceiver = threading.Thread(target=receiver, args=[howowConfig.dbCycle])
    threadSender = threading.Thread(target=sender,args = [howowConfig.dbCycle])

    theadSensor.start()
    threadLED.start()
    threadReceiver.start()
    threadSender.start()
    while True:
        pass
    pass

if __name__ == "__main__":
    main()