# Apresentação do programa de cobrança de serviços da copiadora do Julianno:
print("Bem-vindo à copiadora do Julianno Arthur!")
print("Escolha o serviço abaixo: ")
print("1 - Digitalização(DIG)")
print("2 - Impressão preto e branco(IPB)")
print("3 - Impressão colorida(ICO)")
print("4 - Fotocópia(FOT)")

# Constantes de preços dos serviços:
DIG = 1.10
IPB = 1.00
ICO = 0.40
FOT = 0.50

# Função para exibir erro:
def exibir_erro(mensagem):
    print(mensagem)

# Condicionais do serviço solicitado:
def escolha_serviço():
    while True:
        try:
            serviço = (input("Digite o serviço desejado: ")).strip().upper()

            if serviço == "DIG":
                print(f"Você escolheu o serviço de digitalização: R${DIG:.2f}")
                preço = DIG
                return preço
            elif serviço == "IPB":
                print(f"Você escolheu o serviço de impressão preto e branco: R${IPB:.2f}")
                preço = IPB
                return preço
            elif serviço == "ICO":
                print(f"Você escolheu o serviço de impressão colorida: R${ICO:.2f}")
                preço = ICO
                return preço
            elif serviço == "FOT":
                print(f"Você escolheu o serviço de fotocópia: R${FOT:.2f}")
                preço = FOT
                return preço
            else:
                 exibir_erro("Opção inválida, tente novamente")
        except ValueError:
            exibir_erro("Entrada de serviço inválida, tente novamente.")
            return 0

# Função para calcular o número de páginas:
def num_paginas():
    while True:
        try:
            
            paginas = int(input("Digite o número de páginas desejado: "))
            preco_por_pagina = IPB 
            total = paginas * preco_por_pagina

            if paginas <= 0 or paginas > 20000:
                exibir_erro("Não é aceito essa quantidade de páginas, tente novamente.")
                continue
            elif paginas > 20 and paginas <200:
                desconto = total * 0.15
                total -= desconto
            elif paginas >= 200 and paginas < 2000:
                desconto = total * 0.20
                total -= desconto
            elif paginas >= 2000 and paginas < 20000:
                desconto = total * 0.25
                total -= desconto
            else:
                exibir_erro("por favor, insira a quantidade de páginas novamente")
                continue
            return total
                
        except ValueError:
            exibir_erro("Entrada inválida. Por favor, insira um número válido.")
            continue
    
# Função para serviços extras:
def serviços_extras():
    # Costantes do serviço extra:
    Preço_enc_simples = 15.00
    Preço_enc_capa_dura= 40.00
    try:
        print(" Deseja mais algum serviço?:")
        print("1 - Encardenação simples R$ 15.00")
        print("2 - Encardenação Capa Dura R$ 40.00")
        print("3 - Não desejo mais nada")
        extra = int(input("Insira o número do serviço extra desejado: "))

        if extra == 1:
            preço = Preço_enc_simples
            print("Você escolheu o serviço de encardenação simples.")
        elif extra == 2:
            preço = Preço_enc_capa_dura
            print("Você escolheu o serviço de encardenação Capa Dura.")
        elif extra == 3:
            preço = 0
            print("Nenhum serviço extra solicitado.")
        else:
            exibir_erro("Opção inválida, tente novamente.")
        return preço
    except ValueError:
        exibir_erro("Erro inesperado")
        return 0

# Função principal:
def main():
    valor_serviço = escolha_serviço()
    valor_paginas = num_paginas()
    valor_extra = serviços_extras()
    total = valor_serviço + valor_paginas + valor_extra
    print(f"O valor total do serviço é R${total:.2f}(serviço: {valor_serviço:.2f} + páginas: {valor_paginas:.2f} + extra: {valor_extra:.2f})")
    print("Obrigado por usar os serviços da copiadora do Julianno!")

# Executar o programa:
if __name__ == "__main__":
    main()