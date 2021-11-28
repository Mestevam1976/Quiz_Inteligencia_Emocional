from typing import Any
import matplotlib.pyplot as plt
import mensagens, formatacao, images_ascii
pilar_autoconsciencia = []
pilar_autorregulacao = []
pilar_automotivacao = []
pilar_empatia = []
pilar_habilidades_sociais = []

pontos = []
soma_pontos = sum(pontos)

def encerra():
    exit()

def questoes(num_questao): # lembrando de que o número da questão é igual a n-1
    soma_geral = sum(pilar_autoconsciencia) + sum(pilar_autorregulacao) + sum(pilar_automotivacao) + sum(pilar_empatia) + sum(pilar_habilidades_sociais)
    pontos.append(soma_geral)
    formatacao.forma_linha()
    contador = 0

    if num_questao == 20:
            mensagem_fim_perguntas = 'FIM DAS QUESTÕES'
            print(formatacao.escolher_cor('blue', mensagem_fim_perguntas).center(90)) 
            formatacao.forma_linha()
            mensagem_final = 'O SEU TOTAL DE PONTOS É: '
            print(formatacao.escolher_cor('green',mensagem_final), formatacao.escolher_cor('green',soma_geral))
            return soma_geral
          
    else:
        if num_questao < 20:
            if num_questao == num_questao:
                textos_perguntas = mensagens.questoes[num_questao].upper()
                print(formatacao.escolher_cor('blue', textos_perguntas))
                print(mensagens.opcoes)
                formatacao.forma_linha()

                entrada_ok = False

                while entrada_ok == False:
                    resposta = input('Informe uma das opções acima (digite somente a, b, c, d ou e.): ')
                    valor = 0

                    if resposta.lower() == 'a':
                        valor = 5
                        entrada_ok = True
                    elif resposta.lower() == 'b':
                        valor = 4
                        entrada_ok = True
                    elif resposta.lower() == 'c':
                        valor = 3
                        entrada_ok = True
                    elif resposta.lower() == 'd':
                        valor = 2
                        entrada_ok = True
                    elif resposta.lower() == 'e':
                        valor = 1
                        entrada_ok = True
                    else:
                        texto_alerta = 'Atenção digite somente as letras a, b, c, d ou e!!!'
                        print(formatacao.escolher_cor('yellow', texto_alerta))
                        valor = 0
                        entrada_ok = False           
                    
            
                if num_questao == 0 or num_questao == 7 or num_questao == 12 or num_questao == 17:
                    pilar_autoconsciencia.append(valor)                            
                                                       
                if num_questao == 1 or num_questao == 6 or num_questao == 11 or num_questao == 16:
                    pilar_autorregulacao.append(valor)
                                
                if num_questao == 2 or num_questao == 5 or num_questao == 10 or num_questao == 15:
                    pilar_automotivacao.append(valor)
                                
                if num_questao == 3 or num_questao == 9 or num_questao == 13 or num_questao == 18:
                    pilar_empatia.append(valor)
                            
                if num_questao == 4 or num_questao == 8 or num_questao == 14 or num_questao == 19:
                    pilar_habilidades_sociais.append(valor)    
                                            
        contador += 1
        if contador <= 19:
                questoes_implementa = num_questao + 1
                formatacao.clear()
                print(images_ascii.logo)
                questoes(questoes_implementa)
                return soma_geral
     
def saida_mensagem():
    texto_faixa01 = mensagens.pontos_faixa_01
    texto_faixa02 = mensagens.pontos_faixa_02
    texto_faixa03 = mensagens.pontos_faixa_03
    texto_faixa04 = mensagens.pontos_faixa_04

    if pontos[-1] <= 39:
        print(formatacao.escolher_cor('blue', texto_faixa01.upper()))
    
    elif pontos[-1] > 39 and pontos[-1] < 59:
        print(formatacao.escolher_cor('blue', texto_faixa02.upper()))
    
    elif pontos[-1] > 59 and pontos[-1] < 79:
        print(formatacao.escolher_cor('blue', texto_faixa03.upper()))

    elif pontos[-1] > 79:
        print(formatacao.escolher_cor('blue', texto_faixa04.upper()))
  
def exibe_total_categorias():
    print(formatacao.escolher_cor('red', mensagens.titulos[0]).center(100))
    formatacao.forma_linha()
    print(formatacao.escolher_cor('green', mensagens.titulos[1]), sum(pilar_autoconsciencia))
    print(formatacao.escolher_cor('yellow', mensagens.titulos[2]), sum(pilar_autorregulacao))
    print(formatacao.escolher_cor('blue', mensagens.titulos[3]), sum(pilar_automotivacao))
    print(formatacao.escolher_cor('red', mensagens.titulos[4]), sum(pilar_empatia))
    print(formatacao.escolher_cor('blue', mensagens.titulos[5]), sum(pilar_habilidades_sociais))
    print(formatacao.escolher_cor('green', mensagens.titulos[6]).center(100))

