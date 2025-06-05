import os
import P_Logger
from P_ModelCheckCode import CheckCode
import asyncio

async def CheckAsync(file, lines):
    if not any('M6' in word for word in lines):
        #P_Logger.logger.error("Brak M6 w pliku => " + file)
        return CheckCode(1,file, "P_CheckM6","Brak M6")
    
def Check(file, lines):
    if not any('M6' in word for word in lines):
        #P_Logger.logger.error("Brak M6 w pliku => " + file)
        return CheckCode(1,file, "P_CheckM6","Brak M6")

async def main():    
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
