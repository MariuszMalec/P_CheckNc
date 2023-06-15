import os
import P_Logger
from P_ModelCheckCode import CheckCode

def Check(file, lines):
    g41 = len([match for match in lines if "G41" in match])
    g42 = len([match for match in lines if "G42" in match])
    g40 = len([match for match in lines if "G40" in match])
    #P_Logger.logger.debug("G41/G42/G40 => " + str(g41) + "/" + str(g42) + "/" + str(g40))
    if ( (g41 + g42) != g40):    
       #P_Logger.logger.error(f"Brak korekcji promieniowej! w pliku {file}")
       return CheckCode(1,file, "CheckG41G42G40","Brak korekcji promieniowej")

def main():    
    file = r'c:/tempnc/D12345638.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        Check(file, lines)

if __name__ == '__man__':
    main()    
        
