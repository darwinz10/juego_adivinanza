import pytest
from juego_adivinanza import juego_adivinanza

@pytest.mark.parametrize("intento,numSecreto,numAdivinado",[
    (12,50,-1),
    (78,50,1)
    (36,36,0),

])

def test_evaluar_intento(intento,numSecreto,numAdivinado):
    assert juego_adivinanza(intento,numSecreto) == numAdivinado