import os
import P_Logger
from P_ModelCheckCode import CheckCode
import asyncio


async def CheckAsync(file, machine, lines):    
        if (machine.__contains__("HURON")):
            matches = [match for match in lines if "M30" in match]
            for match in matches:
                if not (match.__contains__("HSTM")):
                    return(CheckCode(5,file, "checkM30","Usun 30 w pliku => " + file))
    
def Check(file, machine, lines):
    if (machine.__contains__("HURON")):
        matches = [match for match in lines if "M30" in match]
        for match in matches:
            if not (match.__contains__("HSTM")):
                return(CheckCode(5,file, "checkM30","Usun 30 w pliku => " + file))
                
async def main():    
    file = r'./Source/D12345685.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        check = await CheckAsync(file, "HSTM300HD", lines)
        if (check == None):
            P_Logger.logger.info("Brak bledow w pliku => " + file)
        if (check):
            P_Logger.logger.error("Bledy w pliku => " + check.error)

if __name__ == '__main__':
    asyncio.run(main())      
