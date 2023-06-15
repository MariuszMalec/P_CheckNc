class CheckCode():
    def __init__(self, id, ncProgramCheck, message, error):
        self.id = id
        self.ncProgramCheck = ncProgramCheck
        self.message = message
        self.error = error
        self.errors = []
    def AddError(self, error):
        return self.errors.append(error)
    def GetErrors(self):
        if (self.errors.Count()>0):
            return self.errors