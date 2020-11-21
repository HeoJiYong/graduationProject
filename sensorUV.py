'''
UV센서
data - 4
'''
print('import :',__name__)
import RPi.GPIO as GPIO
class UVSensor:
    def __init__(self,pinNum):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinNum, GPIO.IN)
        self.pinNum = pinNum
        self.UV = -1
        self.updateData()
        pass

    def updateData(self):
        self.UV = GPIO.input(self.pinNum)
        pass

    def getData(self):
        return self.UV
        pass

def main():
    import howowConfig
    import time
    testSensor = UVSensor(howowConfig.uvPin)
    while True:
        testSensor.updateData()
        print(testSensor.getData())
        time.sleep(3)
        pass
    pass

if __name__ == "__main__":
    main()
    pass