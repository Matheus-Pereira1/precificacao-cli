import pytest
import requests
from src.calculadora import obter_cotacao_dolar

def test_integracao_api_cotacao_sucesso():
    """Valida se a aplicação consegue consultar a API externa com sucesso."""
    cotacao = obter_cotacao_dolar()
    
    # Se a API respondeu, o retorno não pode ser None
    assert cotacao is not None
    # A cotação deve ser um número float e maior que zero
    assert isinstance(cotacao, float)
    assert cotacao > 0

def test_api_status_code():
    """Valida se a URL da API está respondendo com status 200 OK diretamente."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    resposta = requests.get(url, timeout=5)
    assert resposta.status_code == 200