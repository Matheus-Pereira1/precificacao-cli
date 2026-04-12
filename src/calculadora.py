def calcular_preco_venda(custo_materiais, horas_trabalhadas, valor_hora):
    """Calcula o preço justo de venda de um produto."""
    if custo_materiais < 0 or horas_trabalhadas < 0 or valor_hora < 0:
        raise ValueError("Os valores não podem ser negativos.")
    
    custo_mao_de_obra = horas_trabalhadas * valor_hora
    preco_final = custo_materiais + custo_mao_de_obra
    return preco_final

def main():
    print("=== Calculadora de Precificação para Microempreendedores ===")
    print("Descubra o preço justo para vender o seu produto/serviço.\n")
    
    try:
        custo_materiais = float(input("1. Qual o custo total dos materiais? (R$): "))
        horas_trabalhadas = float(input("2. Quantas horas você gastou produzindo?: "))
        valor_hora = float(input("3. Quanto vale a sua hora de trabalho? (R$): "))
        
        preco = calcular_preco_venda(custo_materiais, horas_trabalhadas, valor_hora)
        
        print("\n---------------------------------------------------")
        print(f"💰 O preço sugerido para venda é: R$ {preco:.2f}")
        print("---------------------------------------------------")
    except ValueError as e:
        print(f"\n❌ Erro: Entrada inválida. {e}")

if __name__ == "__main__":
    main()
    