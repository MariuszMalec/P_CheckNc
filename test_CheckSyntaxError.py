import unittest
import P_CheckSyntaxError
import asyncio, time
import Globals as glob
from prettytable import PrettyTable

class Test_P_CheckSyntaxError(unittest.TestCase):

    glob.start_time = time.time()
    glob.table = PrettyTable()
    header = ["NcProgram", "Function","Time"]
    glob.table.field_names = header

    def test_P_CheckSyntaxError_Return_2Errors(self):
        async def run_test():
            file = r'./Source/D12345637.SPF'
            with open(file) as f:
                lines = f.readlines()
                result = await P_CheckSyntaxError.CheckAsync(file, lines)
                self.assertEqual(len(result), 1)
        asyncio.run(run_test())

    def test_P_CheckSyntaxError_Return_ErrorFirst(self):
        async def run_test():
            file = r'./Source/D12345637.SPF'
            with open(file) as f:
                lines = f.readlines()
                result = await P_CheckSyntaxError.CheckAsync(file, lines)
                self.assertEqual(
                    result[0].error,
                    'Nie mozna z parsowac N48 X-148.788 Yaa-20.173 Z-14.447 \n'
                )
        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
