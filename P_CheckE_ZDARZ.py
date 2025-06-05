import os
import P_Logger
from P_ModelCheckCode import CheckCode
import asyncio

async def CheckAsync(file, lines):            
            if file.__contains__("35.SPF") or file.__contains__("49.SPF"):
                if not any("E_ZDARZ=3" in word for word in lines):
                    #P_Logger.logger.error("E_ZDARZ=3 w pliku => " + file)
                    return CheckCode(1,file, "P_CheckE_ZDARZ","E_ZDARZ=3")
    
def Check(file, lines):
        if file.__contains__("35.SPF") or file.__contains__("49.SPF"):
            if not any("E_ZDARZ=3" in word for word in lines):
                #P_Logger.logger.error("E_ZDARZ=3 w pliku => " + file)
                return CheckCode(1,file, "P_CheckE_ZDARZ","E_ZDARZ=3")

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
