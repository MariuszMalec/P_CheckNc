import os
import P_Logger
from P_ModelCheckCode import CheckCode

def Check(file, lines):
    if not any("M17" in word for word in lines):    
        #P_Logger.logger.error("Brak M17 w pliku => " + file)
        return CheckCode(1,file, "checksyntaxerror","Brak M17")
    return CheckCode(1, file, "checksyntaxerror","brak bledow")

def main():    
    file = r'./Source/B12345651.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        Check(file, lines)

if __name__ == '__main__':
    main()        
