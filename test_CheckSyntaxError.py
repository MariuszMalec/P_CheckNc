import unittest
import P_CheckSyntaxError
import asyncio


class Test_P_CheckSyntaxError(unittest.TestCase):

    def test_P_CheckSyntaxError_Return_2Errors(self):
        async def run_test():
            file = r'./Source/D12345637.SPF'
            with open(file) as f:
                lines = f.readlines()
                result = await P_CheckSyntaxError.Check(file, lines)
                self.assertEqual(len(result), 1)
        asyncio.run(run_test())

    def test_P_CheckSyntaxError_Return_ErrorFirst(self):
        async def run_test():
            file = r'./Source/D12345637.SPF'
            with open(file) as f:
                lines = f.readlines()
                result = await P_CheckSyntaxError.Check(file, lines)
                self.assertEqual(
                    result[0].error,
                    'Nie mozna z parsowac N48 X-148.788 Yaa-20.173 Z-14.447 \n'
                )
        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
