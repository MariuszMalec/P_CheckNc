import unittest
import P_CheckSyntaxError


class Test_P_CheckSyntaxError(unittest.TestCase):

    def test_P_CheckSyntaxError_Return_2Errors(self):
        file = r'./Source/D12345637.SPF'
        with open(file) as f:
            lines = f.readlines()
            result = P_CheckSyntaxError.Check(file, lines)
            for item in result:
                errorMessage = item.error
            self.assertEqual(len(result), 2)

    def test_P_CheckSyntaxError_Return_ErrorFirst(self):
        file = r'./Source/D12345637.SPF'
        with open(file) as f:
            lines = f.readlines()
            result = P_CheckSyntaxError.Check(file, lines)
            errorMessage = ""
            for item in result:
                errorMessage = item.error
            self.assertEqual(result[1].error, 'Nie mozna z parsowac N48 X-148.788 Yaa-20.173 Z-14.447 \n')


if __name__ == '__main__':
    unittest.main()
