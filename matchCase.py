'''
Você foi contratado para criar um menu interativo de
atendimento para uma empresa fictícia. O sistema deve exibir as opções abaixo e, de acordo com o número digitado, apresentar uma resposta:

Opções do menu:

[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair

O que o programa deve fazer:

Mostrar o menu acima.
Receber a opção digitada pelo usuário.
Utilizar match case para responder com base na opção.
Exibir uma mensagem apropriada para cada caso.
Caso digite algo inválido, exibir: "Opção inválida, tente novamente!"

Critérios para o desafio estar completo:

Testar diferentes entradas para verificar todas as respostas.
Enviar o link do repositório com o Código

'''

print('''
      Opções do menu:
      
        [1] Falar com atendente
        [2] Segunda via de boleto
        [3] Cancelar serviço
        [4] Informações sobre planos
        [5] Sair
      
      ''')

menu = int(input("Qual sua opção desejada: "))

match menu:
    case 1:
        print("Aguarde o atendente...")
    case 2:
        print("Imprimindo a segunda via do boleto...")
    case 3:
        print("Cancelando serviço...")
    case 4:
        print("Apresentando informações...")
    case _:
        print("Opção invalida")
        
        