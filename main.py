"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    Valor = float(input('Digite um valor entre R$0,00 e R$10,00.'))
    print('São necessárias:')
    Valor = Valor*100
    if Valor // 100 > 0:
      print(f'moedas de R$ 1.00: {Valor//100:.0f}')
      Valor = Valor%100 
    if Valor//50 > 0:
      print(f'moedas de R$ 0.50: {Valor//50:.0f}')
      Valor = Valor%50
    if Valor//25 > 0:
      print(f'moedas de R$ 0.25: {Valor//25:.0f}')
      Valor = Valor%25
    if Valor//10 > 0:
      print(f'moedas de R$ 0.10: {Valor//10:.0f}')
      Valor = Valor%10 
    if Valor//5 > 0:
      print(f'moedas de R$ 0.05: {Valor//5:.0f}')
      Valor = Valor%5
    if Valor//1 > 0:
      print(f'moedas de R$ 0.01: {Valor//1:.0f}')  

if __name__ == '__main__':
    main()
