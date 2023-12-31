import P_Logger, os
from P_ModelCheckCode import CheckCode

errors = []

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False 

def Check(file, lines):     
    errors = []
    linesWithTrans = []
    for line in lines:
        if (line.__contains__("TRANS")) and \
                not (line.startswith(';')):
                    linesWithTrans.append(line)     
    words = ['X','Y','Z','A','B','F']
    for word in words:
        checkWord = word
        for match in linesWithTrans:
            for item in match.split(' '):
                item = item.replace("TRANS","")
                if item.__contains__(word):                    
                    item = item.replace("=-R",'')
                    item = item.replace("=R",'')
                    if not word in item:
                        errors.append(CheckCode(7,file, "checksyntaxerrorinTrans","Musi byc podana os " + match))
                    item = item.replace(word,'')
                    isParse = is_int(item)
                    if not isParse and item != "":  
                        errors.append(CheckCode(7,file, "checksyntaxerrorinTrans","Nie mozna z parsowac " + match))
    return errors

def main():    
    file = r'./Source/D12345620.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        errors = Check(file, lines)
        if (len(errors) == 0):
            P_Logger.logger.info("Brak bledow w pliku => " + file)
        if (len(errors)>0):
            for error in errors:
                P_Logger.logger.error("Bledy w pliku => " + file + ", patrz =>" + str(error.error))

if __name__ == '__main__':
    main()        