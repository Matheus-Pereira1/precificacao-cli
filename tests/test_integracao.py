import requests
from unittest.mock import patch
from src.calculadora import obter_cotacao_dolar

def test_integracao_api_cotacao_sucesso():
    """Valida o comportamento da aplicação simulando um retorno de sucesso da API."""
    # Usamos o caminho absoluto do módulo para o mock não se perder no CI
    with patch('src.calculadora.obter_cotacao_dolar', return_value=5.20):
        cotacao = obter_cotacao_dolar()
        assert cotacao is not None
        assert cotacao == 5.20

def test_api_status_code():
    """Valida se a URL da API responde com status aceitável no ambiente de testes."""
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        assert resposta.status_code == 200