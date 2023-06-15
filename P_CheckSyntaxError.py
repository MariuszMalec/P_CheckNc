from P_ModelCheckCode import CheckCode

errors = []

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def Check(file, lines):    
    errors = []
    linesWithMovments = []
    for line in lines:
        if not (line.__contains__("MSG")) and \
                not (line.startswith(';')) and \
                not (line.__contains__('TRANS')) and \
                not (line.__contains__('TRAFOOF')) and \
                not (line.__contains__('TRAORI')) and \
                not (line.__contains__('E_ZDARZ')) and \
                not (line.__contains__('DELTA')) and \
                not (line.__contains__('CYCLE')) and \
                not (line.__contains__(' - ')) and \
                not (line.__contains__('FGROUP')) and \
                not (line.__contains__('blokada')) and \
                not (line.__contains__('SOFT')) and \
                not (line.__contains__('FNORM')) and \
                not (line.__contains__('ACS')) and \
                not (line.__contains__('OSI')) and \
                not (line.__contains__('wstawione')) and \
                not (line.__contains__('TRAILON')) and \
                not (line.__contains__('NT')) and \
                not (line.__contains__('FS')) and \
                not (line.__contains__('SPIRALA')) and \
                not (line.__contains__('USUN')) and \
                not (line.__contains__('=R')) and \
                not (line.__contains__('R1')) and \
                not (line.__contains__('R2')) and \
                not (line.__contains__('COMPOF')) and \
                not (line.__contains__('FFWON')) and \
                not (line.__contains__('NG')) and \
                not (line.__contains__("VELOLIM")):
                    linesWithMovments.append(line)     
    words = ['X','Y','Z','A','B','F']
    for word in words:
        checkWord = " " + word
        for match in linesWithMovments:
            for item in match.split(' '):
                if item.__contains__(word):
                    item = item.replace("A=DC(","")
                    item = item.replace(")",'')
                    item = item.replace(word,'')
                    isParse = is_float(item)
                    if not isParse:
                        errors.append(CheckCode(7,file, "checksyntaxerror","Nie mozna z parsowac " + match))
    return errors