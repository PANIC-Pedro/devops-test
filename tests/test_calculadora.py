from src.calculadora import soma
from src.calculadora import subtracao
from src.calculadora import multiplicacao

def test_soma():
  assert soma(2 , 3) == 5
  
def test_subtracao():
  assert subtracao(5,3) == 2

def test_multiplicacao():
  assert multiplicacao(5,3) ==15   
