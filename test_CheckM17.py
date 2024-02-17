# content of test_expectation.py
import pytest
import P_CheckM17


@pytest.mark.parametrize("test_input1, test_input2, expected", [(r'./Source/D12345685.SPF', ['N300 M17'], ''),
                                                                (r'./Source/D12345636.SPF', ['N3 G90'], 'Brak M17'),
                                                                (r'./Source/D12345637.SPF', ['N300 '], 'Brak M17')])
def test_p_checkm17(test_input1, test_input2, expected):
    result = P_CheckM17.Check(test_input1, test_input2)
    if (result != None):
        result = result.error
    else:
        result = ''
    assert result == expected
