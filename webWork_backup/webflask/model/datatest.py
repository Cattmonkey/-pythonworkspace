# -*- coding: utf-8 -*-
import sqlite3
class datasql(object):
    def __init__(self):
        self.conn = None
        pass
    def conn(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute('''CREATE TABLE COMPANY(NAME TEXT NOT NULL
                                                        COMMENT TEXT  NOT NULL
                                                        TIME TEXT)''')
        except:
            print("create err");
    def write(self):
        self.cursor.execute
    def read(self):
        if self.conn is None:
            self.conn()
        
        pass
    def close(self):
        pass
    def __del__(self):
        pass

def sq():
  conn=sqlite3.connect('GUEST.db');
     print("opened database successfully") 
     c=conn.cursor()
     print ("Opened database successfully")
     try:
         c.execute('''CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL,
                                         NAME TEXT          NOT NULL,
                                         AGE  INT           NOT NULL,
                                         ADDRESS CHAR(50),
                                         SALARY  REAL);''')
         print('table created successfully')
         for i in range(3, 10):
            print(i)
            c.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
                                   VALUES(" + str(i) + ",'Allen',25,'Texas',1500.00)")
         
     except:
         print("err")
         
     
     cursor=c.execute("SELECT ID,NAME,ADDRESS,SALARY from COMPANY")
     for k in cursor:
         print(k)

    
    

    conn.commit()
     print ("Records created successfully")
     conn.close()
     
 def read():
     w=open("text.txt","w")
     print(" ".join([(i%10 == 0 and i!=0 and str(i) + "\n") 
         or (str(i)) for i in range(0,10000)]))
     w.close()
     
 read()
     

