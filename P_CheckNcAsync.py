import sys
import time, os
import P_Logger
import P_CheckM17, P_CheckSyntaxError, P_CheckSyntaxErrorInTRANS
import P_CheckG41G42G40, P_CheckTraoriPosition, P_CheckM6, P_CheckE_ZDARZ
import P_CheckA360, P_CheckRAPORT, P_CheckM30
from P_ModelCheckCode import CheckCode
import asyncio
from prettytable import PrettyTable # please install: pip install prettytable
import Globals as glob
    
def getMachine(lines):
    matches = [match for match in lines if "MACHINE" in match]
    machine = "-"
    for match in matches:
        if (match.__contains__("HSTM_300HD_SIM840D_Py")):
            machine = "HSTM300HD"
        if (match.__contains__("HSTM_500_SIM840D_Py")):
            machine = "HSTM500HD"  
        if (match.__contains__("HSTM_300_SIM840D_Py")):
            machine = "HSTM300"                        
    return machine

def get_files(path):
    files = []
    for file in os.listdir(path):
        if file.__contains__(".spf") or file.__contains__(".SPF"):
            if os.path.isfile(os.path.join(path, file)):
                files.append(os.path.join(path, file))
    return files

async def main():    
    P_Logger.logger.info('Starting async checking ...')   

    glob.start_time = time.time()
    mainerrors = []
    glob.table = PrettyTable()
    header = ["NcProgram", "Function","Time"]
    glob.table.field_names = header

    #check directory
    #folder = r'./Source'
    folder = r'c:/tempnc'
    if not (os.path.dirname(folder)):
        P_Logger.logger.error('brak katalogu!')
        sys.exit()  

    files = get_files(folder)

    for file in files:

        if (os.path.exists(file)):            

            with open(file) as txt_file:
                lines = [line.rstrip() for line in txt_file]

            machine = getMachine(lines)

            file = os.path.basename(file)

            results = await asyncio.gather(                
                P_CheckM17.CheckAsync(file, lines),
                P_CheckG41G42G40.CheckAsync(file, lines),
                P_CheckTraoriPosition.CheckAsync(file, lines),
                P_CheckSyntaxError.CheckAsync(file, lines),
                P_CheckSyntaxErrorInTRANS.CheckAsync(file, lines),
                P_CheckM6.CheckAsync(file, lines),
                P_CheckE_ZDARZ.CheckAsync(file, lines),
                P_CheckA360.CheckAsync(file, machine, lines),
                P_CheckRAPORT.CheckAsync(file, machine, lines),
                P_CheckM30.CheckAsync(file, machine, lines)
            )  

            # Process the results
            mainerrors.append(results[0])
            mainerrors.append(results[1])
            mainerrors.append(results[2])
            mainerrors.extend(results[3])
            mainerrors.extend(results[4])      
            mainerrors.append(results[5])      
            mainerrors.append(results[6]) 
            mainerrors.append(results[7]) 
            mainerrors.append(results[8]) 
            mainerrors.append(results[9])       

    print(glob.table)

    count=1
    for item in mainerrors:
        if (item != None):
            P_Logger.logger.error(f'{count}, {item.ncProgramCheck}, {item.message} ,=> {item.error}')
            count+=1

    if (len(mainerrors)==0):
        P_Logger.logger.info("Brak bledow")

    P_Logger.logger.info("--- %s seconds ---" % (time.time() - glob.start_time))   

if __name__ == '__main__':
    asyncio.run(main())      

