import os, time
import P_Logger
from P_ModelCheckCode import CheckCode
import asyncio
import Globals as glob
from prettytable import PrettyTable

async def CheckAsync(file, lines):
    start_time = time.time()
    if not any('M17' in word for word in lines):
        #P_Logger.logger.error("Brak M17 w pliku => " + file)
        glob.table.add_row([file,"checkM17","--- %s seconds ---" % (time.time() - start_time)])  
        return CheckCode(1,file, "checkM17","Brak M17")
    glob.table.add_row([file,"checkM17","--- %s seconds ---" % (time.time() - start_time)])  
    
def Check(file, lines):
    if not any('M17' in word for word in lines):
        #P_Logger.logger.error("Brak M17 w pliku => " + file)
        return CheckCode(1,file, "checkM17","Brak M17")

async def main():    

    glob.start_time = time.time()
    glob.table = PrettyTable()
    header = ["NcProgram", "Function","Time"]
    glob.table.field_names = header

    file = r'./Source/D12345685.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        check = await CheckAsync(file, lines)
        if (check == None):
            P_Logger.logger.info("Brak bledow w pliku => " + file)
        if (check):
            P_Logger.logger.error("Bledy w pliku => " + check.error)

if __name__ == '__main__':
    asyncio.run(main())      
