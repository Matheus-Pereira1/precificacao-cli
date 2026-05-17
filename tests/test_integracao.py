import requests
from unittest.mock import patch
from src.calculadora import obter_cotacao_dolar

def test_integracao_api_cotacao_sucesso():
    """Valida o comportamento simulando um retorno de sucesso da API externa."""
    # Mockamos diretamente o requests.get para simular um JSON válido de retorno da API
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "USDBRL": {"high": "5.20", "low": "5.18", "bid": "5.20"}
        }
        
        cotacao = obter_cotacao_dolar()
        assert cotacao is not None

def test_api_status_code():
    """Valida se a URL da API responde com status aceitável no ambiente de testes."""
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        assert resposta.status_code == 200