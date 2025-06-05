import unittest
import asyncio
import P_CheckM17

class TestPCheckM17(unittest.TestCase):

    def test_p_checkm17_cases(self):
        test_cases = [
            (r'./Source/D12345685.SPF', ['N300 M17'], ''),
            (r'./Source/D12345636.SPF', ['N3 G90'], 'Brak M17'),
            (r'./Source/D12345637.SPF', ['N300 '], 'Brak M17')
        ]

        for test_input1, test_input2, expected in test_cases:
            with self.subTest(file=test_input1):
                result = asyncio.run(P_CheckM17.Check(test_input1, test_input2))
                error = result.error if result is not None else ''
                self.assertEqual(error, expected)

if __name__ == '__main__':
    unittest.main()