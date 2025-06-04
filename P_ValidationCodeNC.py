import re, time, os, sys
import P_Logger

# Define allowed G and M codes
VALID_G_CODES = {0, 1, 2, 3, 4, 20, 21, 28, 40, 41, 42, 53, 54, 55, 56, 57, 58, 90, 91, 94}
VALID_M_CODES = {0, 2, 3, 5, 6, 9, 17, 30, 340, 341, 342, 347, 348}
SKIP_VALUE_CODES = {"MSG","CYCLE832","E_ZDARZ","TRAFOOF","TRANS","FGROUP"}
CONVERT_FLOAT_CODES = {'X','Y','Z','A','B','F'}

# Regular expression to match a line of G-code
GCODE_LINE_REGEX = re.compile(r'^([GMT]\d+)?(\s+[NXYZFRS][-+]?\d+(\.\d+)?)*$')

def get_files(path):
    files = []
    for file in os.listdir(path):
        if file.__contains__(".spf") or file.__contains__(".SPF"):
            if os.path.isfile(os.path.join(path, file)):
                files.append(os.path.join(path, file))
    return files

def validate_gcode_line(line):

    line = line.strip().upper()

    if not line or line.startswith('('):  # skip comments or empty lines
        return True
    
    if not line or line.startswith(';'):  # skip comments or empty lines
        return True    
    
    for skipValue in SKIP_VALUE_CODES:
        if skipValue in line:
            return True

    #dont check after ';'
    line = line.split(';')[0]

    tokens = line.split()    

    for token in tokens:
        if token.startswith('G'):
            code = int(token[1:])
            if code not in VALID_G_CODES:
                return False
        elif token.startswith('M'):
            code = int(token[1:])
            if code not in VALID_M_CODES:
                return False            
        elif token[0] not in 'NXYZFRSTABD':
            return False        
        for floatValue in CONVERT_FLOAT_CODES:
            if token.startswith(floatValue):
                try:            
                    code = float(token[1:])
                except ValueError:
                    return False                                                             
    return True

def validate_gcode_file(filepath):
    with open(filepath, 'r') as file:
        for lineno, line in enumerate(file, 1):
            if not validate_gcode_line(line):
                #print(f"Invalid line {lineno}: {line.strip()}")
                P_Logger.logger.error(f"{os.path.basename(filepath)}, Invalid line {lineno}: {line.strip()}")
                return False
    print(f"{os.path.basename(filepath)}, All lines are valid G-code.")
    return True

start_time = time.time()

folder = r'c:/tempnc'
if not (os.path.dirname(folder)):
    P_Logger.logger.error('brak katalogu!')
    sys.exit()  

files = get_files(folder)

for file in files:
    validate_gcode_file(file)

#validate_gcode_file(r'./Source/D12345637.SPF')

print("--- %s seconds ---" % (time.time() - start_time)) 