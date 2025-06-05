import sys
import time, os
import P_Logger
import P_CheckM17, P_CheckSyntaxError, P_CheckSyntaxErrorInTRANS
import P_CheckG41G42G40, P_CheckTraoriPosition
from P_ModelCheckCode import CheckCode
from prettytable import PrettyTable # please install: pip install prettytable

start_time = time.time()
mainerrors = []
table = PrettyTable()
header = ["NcProgram", "Function","Time"]
table.field_names = header
    
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
    
def findErrors(file):
    if (os.path.exists(file)):

        errors = []
        
        with open(file) as txt_file:
            lines = [line.rstrip() for line in txt_file]

        file = os.path.basename(file)

        #----------------------------------------------
        # 1. Get Machine from file
        #----------------------------------------------
        start_time = time.time()
        machine = getMachine(lines)
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time)  + ": check machine")   
        table.add_row([file,"getMachine","--- %s seconds ---" % (time.time() - start_time)])

        P_Logger.logger.debug(f"{file} | {machine}")

        start_time = time.time()
        #----------------------------------------------
        # 2. check E_ZDARZ=3
        #----------------------------------------------
        if file.__contains__("35.SPF") or file.__contains__("49.SPF"):
            if not any("E_ZDARZ=3" in word for word in lines):
                errors.append(CheckCode(2,file, "check_E_ZDARZ3","Brak E_ZDARZ=3 w pliku => " + file))        
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check E_ZDARZ=3")   
        table.add_row([file,"check E_ZDARZ=3","--- %s seconds ---" % (time.time() - start_time)])

        start_time = time.time()
        #----------------------------------------------
        # 3. check M17
        #----------------------------------------------
        errors.append(P_CheckM17.Check(file, lines))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": checkM17") 
        table.add_row([file,"checkM17","--- %s seconds ---" % (time.time() - start_time)])  

        start_time = time.time()
        #----------------------------------------------
        # 4. check G41G42G40
        #----------------------------------------------
        errors.append(P_CheckG41G42G40.Check(file, lines))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check P_CheckG41G42G40")   
        table.add_row([file,"P_CheckG41G42G40","--- %s seconds ---" % (time.time() - start_time)])  

        start_time = time.time()
        #----------------------------------------------
        # 5. check traori
        #----------------------------------------------
        errors.append(P_CheckTraoriPosition.Check(file, lines))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check P_CheckTraoriPosition")     
        table.add_row([file,"P_CheckTraoriPosition","--- %s seconds ---" % (time.time() - start_time)])   

        start_time = time.time()
        #----------------------------------------------
        # 6. check M6
        #----------------------------------------------
        if not any("M6" in word for word in lines):
            errors.append(CheckCode(2,file, "checksyntaxerror","Brak M6 w pliku => " + file))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check M6")   
        table.add_row([file,"check M6","--- %s seconds ---" % (time.time() - start_time)])   

        start_time = time.time()
        #----------------------------------------------
        # 7. check M3
        #----------------------------------------------
        if not any("M03" in word for word in lines) or \
            not any("M3" in word for word in lines):
            errors.append(CheckCode(3,file, "checkM3","Brak M03!"))  
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check M3")   
        table.add_row([file,"check M3","--- %s seconds ---" % (time.time() - start_time)])   

        skipRaport = True
        if not skipRaport:
            start_time = time.time()
            #----------------------------------------------
            # 8. check RAPORT
            #----------------------------------------------
            if (machine.__contains__("HD")):
                matches = [match for match in lines if "RAPORT" in match]
                for match in matches:
                    errors.append(CheckCode(4,file, "checkRAPORT","usun RAPORT! w lini: " + match))      
            #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check RAPORT")  
            table.add_row([file,"check RAPORT","--- %s seconds ---" % (time.time() - start_time)])       

        #----------------------------------------------
        # 9. check M30
        #----------------------------------------------
        if (machine.__contains__("HURON")):
            start_time = time.time()
            matches = [match for match in lines if "M30" in match]
            for match in matches:
                if not (match.__contains__("HSTM")):
                    errors.append(CheckCode(5,file, "checksyntaxerror","Usun 30 w pliku => " + file))
            #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check M30")   
            table.add_row([file,"check M30","--- %s seconds ---" % (time.time() - start_time)])             

        start_time = time.time()
        #----------------------------------------------
        # 10. check A360
        #----------------------------------------------
        if (machine.__contains__("HURON")):
            matches = [match for match in lines if "A=DC(360." in match]
            for match in matches:
                errors.append(CheckCode(5,file, "checkA360","Usun A360 w pliku => " + file))
        else:
            matches = [match for match in lines if "A360." in match]
            for match in matches:
                errors.append(CheckCode(5,file, "checkA360","Usun A360 w pliku => " + file))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time) + ": check A360")   
        table.add_row([file,"check A360","--- %s seconds ---" % (time.time() - start_time)])             

        start_time = time.time()
        #----------------------------------------------
        # 11. check syntaxerror
        #----------------------------------------------
        if not file.__contains__("61.SPF"):
            errors.extend(P_CheckSyntaxError.Check(file, lines))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time)+ ": check P_CheckSyntaxError") 
        table.add_row([file,"P_CheckSyntaxError","--- %s seconds ---" % (time.time() - start_time)])               

        start_time = time.time()
        #----------------------------------------------
        # 12. check syntaxerrorinTRANS
        #----------------------------------------------
        errors.extend(P_CheckSyntaxErrorInTRANS.Check(file, lines))
        #P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time)+ ": check P_CheckSyntaxErrorInTRANS")   
        table.add_row([file,"P_CheckSyntaxErrorInTRANS","--- %s seconds ---" % (time.time() - start_time)])               
           
    else:
        P_Logger.logger.error(f'brak pliku {file}!')
    return errors

def main():    
    P_Logger.logger.info('Starting sync checking ...')   

    #check directory
    #folder = r'./Source'
    folder = r'c:/tempnc'
    if not (os.path.dirname(folder)):
        P_Logger.logger.error('brak katalogu!')
        sys.exit()  

    files = get_files(folder)

    for item in files:
        mainerrors.extend(findErrors(item))
        #P_Logger.logger.debug(item)

    print(table)

    count=1
    for item in mainerrors:
        if (item != None):
            P_Logger.logger.error(f'{count}, {item.ncProgramCheck}, {item.message} ,=> {item.error}')
            count+=1

    if (len(mainerrors)==0):
        P_Logger.logger.info("Brak bledow")

    P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time))   

if __name__ == '__main__':
    main()

