# Rentabilidade mensagem, em %
# Transformando a porcentagem em valor numérico
# Tempo de investimento
from time import sleep

list = []
dados = {}
def linha():
    print('•' * 25)

def escreva(txt):
    tam = len(txt) + 4
    print('\033[40m~\033[m' * tam)
    print(f'\033[40m  {txt}  \033[m')
    print('\033[40m~\033[m' * tam)

sleep(1)
escreva('Investimento')
while True:
    sleep(0.5)
    print(f'\033[40mAperte\033[30m \033[44m[1]\033[40m \033[35mpara você ver um grafico de como organizar seu dinheiro.\033[m '
            '\n\033[40mAperta\033[30m \033[44m[2]\033[40m \033[35mse quiser fazer uma probabilidade do valor que quer investir.\033[m'
            '\n\033[40mAperta\033[30m \033[44m[3]\033[40m \033[35mse quiser fazer com bases nos seu salario.\033[m')

    pergunta2 = str(input('\033[40mdigite aqui:\033[m'))
    linha()
    if pergunta2 == '1':
        sleep(0.1)
        dados['salario'] = float(input('\033[35mQuantos você ta recebendo:R$\033[m'))
        linha()
        essencial = dados['salario'] * 0.5
        investimento = 0.3
        gastar = 0.20
        s = dados['salario'] * investimento
        a = dados['salario'] * gastar
        sleep(1)
        escreva('    Organize sua vida financeira!!   ')
        sleep(1)
        print(f'\033[40mEm essenciais você terá que gastar: \033[35mR${essencial}\033[m\033[40m')
        sleep(2)
        print(f'\033[40mVocê tem para investir: \033[32mR${s}\033[m\033[40m')
        sleep(2)
        print(f'\033[40mVocê pode gastar até: \033[31mR${a:.1f}\033[m\033[40m')
        print('\033[40m-=\033[m' * 30)
        sleep(0)
        while True:
            resp = str(input('Quer continuar?[s/n]: ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('Escreva S/N: ')
        if resp == 'N':
            break
    if pergunta2 == '2':
        sleep(1)
        escreva('\033[40mColoque os valores, retabilidade mensal (%) e os meses\033[m ')
        dados.clear()
        linha()
        sleep(1.3)
        dados['valor inicial '] = float( input('\033[35mValor inicial($):R$\033[m') )
        sleep(1.3)
        dados['rentabilidade mesal '] = float ( input('\033[35mRentabilidade mensal(%):\033[m ') )
        sleep(1.3)
        i = dados['rentabilidade mesal '] / 100
        dados['Meses'] = int( input('\033[35mMeses que vai deixar rendendo:\033[m ') )
        dados['total investido '] = dados['valor inicial '] * (1+i)**dados['Meses']
        composto = dados['valor inicial '] * dados['total investido ']
        list.append(dados.copy())
        linha()
        linha()
        for p in list:
            for v, k in p.items():
                print(f'\033[40m{v}={k:.1f}\33[40m')
            print('-=' * 30)
        while True:
            resp = str(input('\033[35mQuer continuar?[s/n]:\033[35m ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('\033[31mEscreva S/N:\033[m ')
        if resp == 'N':
            break
    if pergunta2 == '3':
        dados['valor inicial '] = float(input('\033[35mSalario($):R$\033[m'))
        investimento = 0.3
        dados['investimento'] = dados['valor inicial '] * investimento
        print(f'\033[41m \033[30mPode investir \033[30m{dados["investimento"]}\033[41m por mês!\033[m')
        sleep(1.3)
        dados['rentabilidade mesal(%) '] = float(input('\033[35mRentabilidade mensal(%):\033[m '))
        sleep(1.3)
        i = dados['rentabilidade mesal(%) '] / 100
        dados['Meses'] = int(input('\033[35mMeses que vai deixar rendendo:\033[m '))
        dados['total investido '] = dados['investimento'] * (1 + i) ** dados['Meses']
        composto = dados['valor inicial '] * dados['total investido ']
        list.append(dados.copy())
        linha()
        print(f'\033[40mSeu salario é de \033[32mR${dados["valor inicial "]}\033[40m reias\033[m')
        print(f'\033[40mRecomendo que invista \033[31mR${dados["investimento"]} \033[m\033[40mreais, que equivale \033[31m30%\033[40m do seu salario\033[m')
        print(f'\033[40mSe você investir \033[35mR${dados["investimento"]} \033[m\033[40m por \033[35m{dados["Meses"]}\033[40m meses... \033[m')
        print(f'\033[40mPode ganhar um retorno estimado em \033[32mR${dados["total investido "]:.2f} \033[m\033[40m '
              f'com dinheiro redendo \033[35m%{dados["rentabilidade mesal(%) "]} \033[m\033[40m ao mês!\033[m')
        while True:
            resp = str(input('\033[35mQuer continuar?[s/n]:\033[35m ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('\033[31mEscreva S/N:\033[m ')
        if resp == 'N':
            break


    if pergunta2 == '0':
        print(f'\033[31mprograma finalizado.\033[31m')
        break


