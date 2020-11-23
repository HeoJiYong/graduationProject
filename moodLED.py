'''
LED
'''
print('import :',__name__)
import board
import neopixel
'''
pinNumber = 60
b = 100
pixels = neopixel.NeoPixel(board.D10,pinNumber,brightness=1,auto_write=False)
for i in range(0,pinNumber):
    pixels[i] = [0,0,0]
pixels.show()
'''
on = 150    #너무 밝으면 이 값을 조정 (0~255)
class LED:
    def __init__(self,pinNum,pixelNum):
        '''
        :param pinNum: 핀 번호
        :param pixelNum: led갯수
        '''
        #0:끈거   |   1:흰색    |   2:빨강    |   3:초록    |
        #4:파랑   |   5:노란    |   6:하늘    |   7:보라    |
        self.colors = [[0,0,0],[on,on,on],[on,0,0],[0,on,0],
                       [0,0,on],[on,on,0],[0,on,on],[on,0,on]]
        self.pinNum=pinNum      #핀번호
        self.pixelNum = pixelNum#led 갯수
        self.pixels=neopixel.NeoPixel(board.D10,pixelNum,brightness=1,auto_write=False) #neopixel 객체생성
        self.rgbIndex = -1      #미리 정의된 led색깔 가르킬 index
        self.isLedOn = True    #led 꺼졌는지 판별할 변수
        self.ledOff()
        pass

    #무드등 색 업데이트
    def updateColor(self,rgbIndex):
        if self.rgbIndex != rgbIndex:    #색이 달라졌을때만 작동 (부하 줄여야함)
            for i in range(0,self.pixelNum):    #새로운 색깔로 바꿔준다(LED 갯수만큼)
                self.pixels[i] = self.colors[rgbIndex]  #pixel 객체에 색깔 적용
            self.rgbIndex = rgbIndex    #현재색깔을 바꿔준다
        self.isLedOn = False
        pass

    #led on
    def ledOn(self):
        if not self.isLedOn:
            self.pixels.show()  #켠다
            self.isLedOn = True #켠 상태로 저장
            print('led On')
        pass

    #led off
    def ledOff(self):
        if self.isLedOn:
            self.updateColor(0) #램프색을 0으로 설정
            self.ledOn()        #끈다
            self.isLedOn = False#끈 상태로 저장
            print('led Off')
        pass

def main():
    import howowConfig
    import time
    testLED = LED(howowConfig.ledPin,howowConfig.ledNum)
    for i in range(0,8):
        testLED.updateColor(i)
        testLED.ledOn()
        time.sleep(1)

    testLED.ledOff()
    pass


if __name__ == "__main__":
    main()
    pass

'''
pixel.fill((255,255,255))
pixel.show()
#pixel.stop()
time.sleep(1)
#pixel.fill((0,0,0))
#pixel.show()
#
#pixel.cleanup()

def main():
    import howowConfig
    import time
    #import keyboard
    testLED = LED(howowConfig.ledPin,howowConfig.ledNum)
    testColors = [[100,0,0],[0,100,0],[0,0,100],[0,0,0]]
    i=0
    for i in range(len(testColors)):
        testLED.updateColor(testColors[i])
        testLED.ledOn()
        time.sleep(2)
    testLED.updateColor([0,0,0])
    testLED.ledOn()
    print('done')
    pass
'''

