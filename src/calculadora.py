import requests

def calcular_preco_venda(custo_materiais, horas_trabalhadas, valor_hora):
    """Calcula o preço justo de venda de um produto."""
    if custo_materiais < 0 or horas_trabalhadas < 0 or valor_hora < 0:
        raise ValueError("Os valores não podem ser negativos.")
        
    custo_mao_de_obra = horas_trabalhadas * valor_hora
    return custo_materiais + custo_mao_de_obra

def obter_cotacao_dolar():
    """Consome a API Pública AwesomeAPI para obter a cotação atual do Dólar (USD)."""
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            return float(dados["USDBRL"]["bid"])
        return None
    except requests.RequestException:
        return None

def main():
    print("=== Calculadora de Precificação para Microempreendedores ===")
    print("Descubra o preço justo para vender o seu produto/serviço.\n")
    
    try:
        custo_materiais = float(input("1. Qual o custo total dos materiais? (R$): "))
        horas_trabalhadas = float(input("2. Quantas horas você gastou produzindo?: "))
        valor_hora = float(input("3. Quanto vale a sua hora de trabalho? (R$): "))
        
        preco_brl = calcular_preco_venda(custo_materiais, horas_trabalhadas, valor_hora)
        
        print("\n-------------------------------------------")
        print(f"💰 O preço sugerido para venda é: R$ {preco_brl:.2f}")
        
        print("🔄 Buscando cotação do Dólar em tempo real para exportação...")
        cotacao_usd = obter_cotacao_dolar()
        
        if cotacao_usd:
            preco_usd = preco_brl / cotacao_usd
            print(f"💵 Preço sugerido convertido: $ {preco_usd:.2f} USD (Cotação: R$ {cotacao_usd:.2f})")
        else:
            print("⚠️ Não foi possível obter a cotação em tempo real no momento.")
        print("-------------------------------------------")
        
    except ValueError as e:
        print(f"\n❌ Erro: Entrada inválida. {e}")

if __name__ == "__main__":
    main()