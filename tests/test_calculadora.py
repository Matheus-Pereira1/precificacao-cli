import pytest
from src.calculadora import calcular_preco_venda

def test_calculo_correto():
    # Caminho feliz: 50 de material + 2 horas a 20 reais/hora = 90
    resultado = calcular_preco_venda(50.0, 2.0, 20.0)
    assert resultado == 90.0

def test_calculo_zero_horas():
    # Caso limite: produto sem tempo de produção contabilizado
    resultado = calcular_preco_venda(30.0, 0.0, 15.0)
    assert resultado == 30.0

def test_valores_negativos():
    # Entrada inválida: tentar passar valor negativo deve gerar erro
    with pytest.raises(ValueError):
        calcular_preco_venda(-10.0, 2.0, 20.0)