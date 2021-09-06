import pymysql

class DBhandler:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def InsertRecord(self,username,score):
        mydb = None
        try:
            successFullyInserted = True
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            query = 'INSERT into game VALUES(%s,%s)'
            args = (username, score)

            mydbCursor.execute(query, args)
            mydb.commit()
            return successFullyInserted
        except Exception as e:
            successFullyInserted = False
            return successFullyInserted
        finally:
            if mydb != None:
                mydb.close()

    def getAllRecords(self):
        mydb = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            query = 'select * from game order by score'

            mydbCursor.execute(query)
            result = mydbCursor.fetchall()
            usersList = []

            for x in result:
                singleDict = {}
                singleDict["username"] = x[0]
                singleDict["score"] = x[1]
                usersList.append(singleDict)

            return usersList
        except Exception as e:
            return []
        finally:
            if mydb != None:
                mydb.close()

