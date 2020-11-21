'''
온습도 센서
'''
print('import :',__name__)
import Adafruit_DHT

class DHTSensor:
	def __init__(self,pinNum):
		self.pinNum = pinNum
		self.humidity = -1
		self.temperature = -1
		self.sensor = Adafruit_DHT.DHT11
		self.updateData()
		pass

	def updateData(self):
		h,t = Adafruit_DHT.read(self.sensor,self.pinNum)
		#값이 제대로 들어왔을때만 저장
		if h and t:
			self.humidity = h
			self.temperature =t
		pass

	def getDatas(self):
		return self.humidity,self.temperature
		pass



def main():
	import howowConfig
	import time
	testSensor = DHTSensor(howowConfig.dhtPin)
	while True:
		testSensor.updateData()
		습도,온도 = testSensor.getData()
		print("Humidity= ", 습도, "  Temperature= ", 온도)
		time.sleep(5)
	pass

if __name__ == "__main__":
	main()
	pass
