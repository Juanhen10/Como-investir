c = ('\033[m', #sem cor
     '\033[0;30;41m', # 1 - fonte: preta; fundo: vermelho
     '\033[0;30;42m', # 2 - fonte: preta; fundo; verde
     '\033[0;30;43m', # 3 - fonte: preta; fundo; amarela
     '\033[0;30;44m', # 4 - fonte: preta; fundo; azul
     '\033[0;30;45m', # 5 - fonte: preta; fundo roxo
     '\033[7;30m',    # 6 - branco
     '\033[40;32m',   # 7 - preto com verde
     '\033[40;35m')   # 8 - preto com roxo

def linha():
    print('\033[40;35m  •\033[m' * 25)

def escreva(txt, cor = 0):
    tam = len(txt) * 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')

def escreva2(txt, cor = 0):
    print(c[cor],end='')
    print(f' {txt}')
    print(c[0], end='')
