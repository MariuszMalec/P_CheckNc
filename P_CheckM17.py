import os
import P_Logger
from P_ModelCheckCode import CheckCode

def Check(file, lines):
    if not any('M17' in word for word in lines):
        #P_Logger.logger.error("Brak M17 w pliku => " + file)
        return CheckCode(1,file, "checksyntaxerror","Brak M17")

def main():    
    file = r'./Source/D12345685.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        check = Check(file, lines)
        if (check == None):
            P_Logger.logger.info("Brak bledow w pliku => " + file)
        if (check):
            P_Logger.logger.error("Bledy w pliku => " + check.error)

if __name__ == '__main__':
    main()        
