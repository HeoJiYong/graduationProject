'''
'''
import pymysql
from howowConfig import *

class infomationDAO():

    #생성자
    def __init__(self,host,user,password,db,charset,port):
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    db=db,
                                    charset=charset,
                                    port=port)
        #self.cur = self.conn.cursor()
        pass

    #select 문
    def select(self,query = 'select * from howow',lang='kor'):
        curs =self.conn.cursor()
        query = query
        curs.execute(query)
        rows = curs.fetchall()

        if lang == 'kor':
            rows = list(rows[0])
            tempArr = []
            for i in rows:
                if type(i) == bytes:
                    i = i.decode('utf-8')
                tempArr.append(i)
            #self.data = tempArr
            rows = tempArr
        self.conn.commit()
        return rows
        pass

    #UV, humidity, temperature 업데이트
    def update(self,query='update howow set',uv=0,humidity=0.0,temperature=0.0):
        curs = self.conn.cursor()
        sql = query +' uv = '+str(int(uv))+', humidity = '+str(float(humidity))+', temperature = '+str(float(temperature)) + ' where 1'
        print(sql)
        curs.execute(sql)
        self.conn.commit()
        pass

    #test용
    def test(self):
        print(self.data)
        pass

    #소멸자
    def __del__(self):
        print('del : ',self.__class__.__name__)
        pass

def main():
    import time
    testdb = infomationDAO(host,user,password,db,charset,port)

    while True:
        print(testdb.select(lang='kor'))
        time.sleep(1)
        pass

    '''
    while True:

        print(testdb.select(lang='kor'))
        time.sleep(1)

        testdb.update('update howow set userinfo = "test1" where 1')
        time.sleep(1)
        print(testdb.select())
        time.sleep(1)

        testdb.update('update howow set userinfo = "test2" where 1')
        time.sleep(1)
        print(testdb.select())
        time.sleep(1)

        testdb.update('update howow set userinfo = "test3" where 1')
        time.sleep(1)
        print(testdb.select())
        time.sleep(1)
        print('end\n')
    '''
    pass


if __name__ == "__main__":
    main()