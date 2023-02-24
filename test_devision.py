from my_funcs.utils import devision
import pytest

@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 2, 10),
                                          (40, 2, 20),
                                          (120, -2, -60)])
def test_def_good(a, b, result):
    assert devision(a, b) == result
    
    
    
@pytest.mark.parametrize("except_err, divider", [(ZeroDivisionError, 0),
                                             (TypeError, '2')])
def test_zero_dev(except_err, divider):
    with pytest.raises(except_err):
        devision(5, divider)
        
        