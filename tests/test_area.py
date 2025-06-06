import pytest
from area import calcular_area

def test_area_valida():
    assert calcular_area(5, 7) == 17.5

def test_base_cero():
    with pytest.raises(ValueError, match="base"):
        calcular_area(0, 7)

def test_altura_negativa():
    with pytest.raises(ValueError, match="negativa"):
        calcular_area(5, -3)

def test_base_y_altura_negativas():
    with pytest.raises(ValueError, match="Ambos valores"):
        calcular_area(-5, -2)
