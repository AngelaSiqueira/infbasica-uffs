def resumo():
    mensagem = "Grace Brewster Murray Hopper nasceu em Nova York, EUA, em 1906. Sendo a criadora das primeiras linguagens computacionais “humanas”, que possibilitou a interpretação computacional de comando em inglês no lugar de apenas números e símbolos."
    return mensagem


def doutorado():
    mensagem = "Esta norte-americana obteve um doutorado em Matemática por Yale em 1934 e, quando os EUA entraram na Segunda Guerra Mundial, abandonou seu trabalho de professora de matemática e ingressou na Marinha, onde chegou à patente de contra-almirante."
    return mensagem


def contribuicoes():
    mensagem = "Criou a Linguagem Comum Orientada para Negócios (COBOL, na sigla em inglês), a primeira linguagem complexa de computador, que é utilizada até hoje por empresas de todo o mundo. Também ficou conhecida por ter batizado o primeiro bug de computador da história."
    return mensagem


def artigos():
    mensagem = "Artigos dela? não achei"
    return mensagem


def citacoes():
    mensagem = "Se é uma boa ideia, prossiga e leve-a adiante. É muito mais fácil pedir desculpas do que conseguir a permissão necessária.\nPara mim Programação é mais do que uma arte prática importante. É também um empreendimento gigantesco nos fundamentos do conhecimento.\nHumans são alérgicos para mudar. Eles adoram dizer: 'Nós sempre fizemos assim.' Eu tento lutar isso. É por isso que eu tenho um relógio na minha parede que corre no sentido anti-horário."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
