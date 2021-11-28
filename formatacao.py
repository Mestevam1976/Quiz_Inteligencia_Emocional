from os import system, name 

def clear():  # Limpa a tela removendo do prompt as informações sobre a localização dos arquivos
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def forma_linha():  # Imprime linha com o caractere =
    print('=' * 80)

def p():  # Pula uma linha
    print('\n')

def cabecalhoI():  # Imprime o cabeçalho inicial do jogo
    forma_linha()

    forma_linha()

def escolher_cor(cor, texto): # função para definir as cores das mensagens
    if cor == 'red':
        return f'\033[91m {texto} \033[0m'

    if cor == 'blue':
        return f'\033[94m {texto} \033[0m'

    if cor == 'yellow':
        return f'\033[93m {texto} \033[0m'

    if cor == 'green':
        return f'\033[92m {texto} \033[0m'

cor_erro = "red"
cor_principal = "blue"
cor_alerta = 'yellow'
cor_sucesso = 'green'