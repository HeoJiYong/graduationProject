#-*- coding: utf-8 -*-
'''
-온도
20이하 추움
21이상 적당
31이상 더움

-습도
90이하 건조함
91이상 적당함
131이상 습함

-햇빛 (자외선)
0(햇빛없음) : 햇빛이 필요해요
1(햇빛있음) :
'''
class flowerState():
    def __init__(self):
        self.state='default State'
        self.temperatureStates = [['추워요','춥고 '],['',''],['더워요','덥고 ']]
        self.humidityStates=[['건조해요','건조하고 '],['',''],['습해요','습하고 ']]
        self.uvStates=['햇빛이 필요해요','']
        pass

    def updateFlowerState(self,temperature,humidity,uv):
        temperatureIndex = [0,1]
        humidityIndex = [0,0]
        uvIndex = 0

        if temperature >= 21:       #21도 이상 이면
            temperatureIndex[0] += 1#'' (=적당함)
            if temperature >= 31:           #31도 이상이면
                temperatureIndex[0] += 1    #더워요

        if humidity >=91:           #습도91이상이면
            temperatureIndex[1]=0  #'더워요' -> '덥고' 로 바꿈
            humidityIndex[0]+=1     #'' (=적당함)
            if humidity >=131:          #습도 131이상이면
                temperatureIndex[1] = 1
                humidityIndex[0] += 1   #습해요
                pass
            pass

        if uv==1:       #햇빛이 있다면
            uvIndex+=1  #'햇빛이 필요해요' -> '' 로 바꿈
        else:
            humidityIndex[1]+=1

        if temperatureIndex[0] ==1 and humidityIndex[0]==1 and uv==1:
            self.state = '기분이 좋아요'
        else:
            self.state=self.temperatureStates[temperatureIndex[0]][temperatureIndex[1]] + self.humidityStates[humidityIndex[0]][humidityIndex[1]] + self.uvStates[uv]
        pass

    def getFlowerState(self):
        return self.state
    def __del__(self):
        pass

def main():
    import time
    #테스트 클래스 인스턴스만들기
    test = flowerState()
    # getFlowerState에 온도 습도 햇빛주기
    test.updateFlowerState(19,45,0)
    print(test.getFlowerState())
    time.sleep(1)

    test.updateFlowerState(25,91,1)
    print(test.getFlowerState())
    time.sleep(1)

    test.updateFlowerState(43,134,1)
    print(test.getFlowerState())
    time.sleep(1)

    test.updateFlowerState(43,134,0)
    print(test.getFlowerState())
    time.sleep(1)

    test.updateFlowerState(43,100,1)
    print(test.getFlowerState())
    pass

if __name__ == '__main__':
    main()