import sqlite3
from datetime import datetime

class Connecter:
    __conn=any
    __cursor=any
    
    def __init__(self, database: str="CoolcatDB"):
        """
        Constructor.

        Parameters:
            database (str) deafault:CoolcatDB
        """
        __dbPath = f'./database/{database}.db'
        self.__conn = sqlite3.connect(__dbPath)
        self.__cursor = self.__conn.cursor() 


    # region function
    def SearchMonthCar(self, month: int=0):
        """
        This function search car in month.

        Parameters:
            month (int) range between 1 to 12
        """
        formattedDate = ''
        currentDate = datetime.now()
        
        if month > 0 and month < 13:
            formattedDate = '{}-{:02d}'.format(currentDate.year, month)
        else:
            formattedDate = currentDate.strftime('%Y-%m')
        
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName WHERE M.PlannedDate LIKE '{formattedDate}%'")    
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)
            
            
    def SearchCarName(self, carName: str):
        """
        This function search car with Name.

        Parameters:
            carName (str)
        """
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName WHERE M.CarName='{carName}'")    
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)
                
                
    # def CreateCar(self, CarName: str, PlannedDate: str):
    #     """
    #     This function Create a new car.

    #     Parameters:
    #         CarName (str)
    #         PlannedDate (str) format 'yyyy-mm-dd'
    #     """
    #     self.__cursor.execute(f"INSERT INTO BlackCar (CarName, Finished, PlannedDate) VALUES ({CarName}, 'N', {PlannedDate})")
    #     self.__conn.commit()

    # def JoinCar(self):  
    #     """
    #     This function calculates the area of a rectangle.

    #     Parameters:
    #         length (float): The length of the rectangle.
    #         width (float): The width of the rectangle.

    #     Returns:
    #     """
    #     self.__cursor.execute("INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName) VALUES ('CarA', 1, 'Player1')")
    #     self.__conn.commit()
    # endregion


x = Connecter('CoolcatDB')