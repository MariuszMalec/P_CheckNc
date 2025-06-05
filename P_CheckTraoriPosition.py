import os
import P_Logger
from P_ModelCheckCode import CheckCode
import asyncio

async def CheckAsync(file, lines):
    traori = [match for match in lines if "TRAORI" in match]
    if len(traori) > 0:
        trafoof = []
        for idx, line in enumerate(lines):
            if (line.__contains__("TRAFOOF")):
                #P_Logger.logger.debug(f"{idx} {line}")
                trafoof.append(idx)
        nmbcheckblock = 20 #obszar szukania TRAORI
        for x in range(len(trafoof)):
                cheklist = lines[trafoof[x]:trafoof[x]+nmbcheckblock]  
                traori=[]
                for n, item in enumerate(cheklist):
                    #P_Logger.logger.debug(f"{n} {item}")
                    if (item.__contains__("TRAORI")):
                        traori.append(True)
                    if not item.startswith(";") and not item.__contains__("G53"):
                        if (item.__contains__(" X")) and \
                            (item.__contains__(" Y")) and \
                            (item.__contains__(" Z")):
                            #P_Logger.logger.debug(f"{n} {item}")
                            if not True in traori:
                                #P_Logger.logger.error(f"Brak TRAORI! w pliku {file}")
                                return CheckCode(1,file, "P_CheckTraoriPosition","Brak TRAORI!")
                            break        

def Check(file, lines):
    traori = [match for match in lines if "TRAORI" in match]
    if len(traori) > 0:
        trafoof = []
        for idx, line in enumerate(lines):
            if (line.__contains__("TRAFOOF")):
                #P_Logger.logger.debug(f"{idx} {line}")
                trafoof.append(idx)
        nmbcheckblock = 20 #obszar szukania TRAORI
        for x in range(len(trafoof)):
                cheklist = lines[trafoof[x]:trafoof[x]+nmbcheckblock]  
                traori=[]
                for n, item in enumerate(cheklist):
                    #P_Logger.logger.debug(f"{n} {item}")
                    if (item.__contains__("TRAORI")):
                        traori.append(True)
                    if not item.startswith(";") and not item.__contains__("G53"):
                        if (item.__contains__(" X")) and \
                            (item.__contains__(" Y")) and \
                            (item.__contains__(" Z")):
                            #P_Logger.logger.debug(f"{n} {item}")
                            if not True in traori:
                                #P_Logger.logger.error(f"Brak TRAORI! w pliku {file}")
                                return CheckCode(1,file, "P_CheckTraoriPosition","Brak TRAORI!")

async def main():    
    file = r'./Source/D12345633.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        check = await CheckAsync(file, lines)
        if (check == None):
            P_Logger.logger.info("Brak bledow w pliku => " + file)
        if (check):
            P_Logger.logger.error("Bledy w pliku => " + file + ", " + check.error)


if __name__ == '__main__':
    asyncio.run(main())    