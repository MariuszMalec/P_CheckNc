from P_ModelCheckCode import CheckCode
import P_Logger, os, time
import asyncio
import Globals as glob
from prettytable import PrettyTable

errors = []

def validate_gcode_line(line):
    
    SKIP_VALUE_CODES = {"MSG","CYCLE832","E_ZDARZ","TRAFOOF","TRANS","FGROUP","B_DREH"}

    line = line.strip()

    if not line or line.startswith('('):
        return None
    
    if not line or line.startswith(';'):
        return None
    
    for skipValue in SKIP_VALUE_CODES:
        if skipValue in line:
            return None
    
    return line

async def CheckAsync(file, lines):    
    start_time = time.time()
    errors = []
    CONVERT_FLOAT_CODES = {'X','Y','Z','A','B','F'}

    for line in lines:

        validateLine = validate_gcode_line(line)

        if validateLine != None:

            validateLine = validateLine.split(';')[0]

            tokens = validateLine.split()    

            for token in tokens:
        
                for floatValue in CONVERT_FLOAT_CODES:
                    if token.startswith(floatValue):
                        try:            
                            code = float(token[1:])
                        except ValueError:
                            errors.append(CheckCode(7,file, "checksyntaxerror","Nie mozna z parsowac " + line))
                            #P_Logger.logger.error(f"checksyntaxerror, Nie mozna z parsowac {line} w pliku {file}")
                            glob.table.add_row([file,"checksyntaxerror","--- %s seconds ---" % (time.time() - start_time)])  
                            return errors                            
    glob.table.add_row([file,"checksyntaxerror","--- %s seconds ---" % (time.time() - start_time)])         
    await asyncio.sleep(0)                 
    return errors

def Check(file, lines):    
    errors = []
    CONVERT_FLOAT_CODES = {'X','Y','Z','A','B','F'}

    for line in lines:

        validateLine = validate_gcode_line(line)

        if validateLine != None:

            validateLine = validateLine.split(';')[0]

            tokens = validateLine.split()    

            for token in tokens:
        
                for floatValue in CONVERT_FLOAT_CODES:
                    if token.startswith(floatValue):
                        try:            
                            code = float(token[1:])
                        except ValueError:
                            errors.append(CheckCode(7,file, "checksyntaxerror","Nie mozna z parsowac " + line))
                            return errors                            
    return errors

async def main():    

    glob.start_time = time.time()
    glob.table = PrettyTable()
    header = ["NcProgram", "Function","Time"]
    glob.table.field_names = header

    file = r'./Source/D12345637.SPF'
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

    with open(file) as f:
        lines = f.readlines()
        errors = await CheckAsync(file, lines)
        if (len(errors) == 0):
            P_Logger.logger.info("Brak bledow w pliku => " + file)
        if (len(errors)>0):
            for error in errors:
                P_Logger.logger.error("Bledy w pliku => " + file + ", patrz =>" + str(error.error))

if __name__ == '__main__':
    asyncio.run(main())          
