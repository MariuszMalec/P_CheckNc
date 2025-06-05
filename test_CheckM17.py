import unittest
import asyncio
import P_CheckM17, time
import Globals as glob
from prettytable import PrettyTable

class TestPCheckM17(unittest.TestCase):

    glob.start_time = time.time()
    glob.table = PrettyTable()
    header = ["NcProgram", "Function","Time"]
    glob.table.field_names = header

    def test_p_checkm17_cases(self):
        test_cases = [
            (r'./Source/D12345685.SPF', ['N300 M17'], ''),
            (r'./Source/D12345636.SPF', ['N3 G90'], 'Brak M17'),
            (r'./Source/D12345637.SPF', ['N300 '], 'Brak M17')
        ]

        for test_input1, test_input2, expected in test_cases:
            with self.subTest(file=test_input1):
                result = asyncio.run(P_CheckM17.CheckAsync(test_input1, test_input2))
                error = result.error if result is not None else ''
                self.assertEqual(error, expected)

if __name__ == '__main__':
    unittest.main()