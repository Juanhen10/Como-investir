# Rentabilidade mensagem, em %
# Transformando a porcentagem em valor numérico
# Tempo de investimento
from time import sleep
from projetinhos.Finanças.design.Design import escreva, linha, escreva2
list = []
dados = {}

sleep(1)
escreva('Investimento',8)
while True:
    sleep(0.5)
    escreva(f' Aperte [1] se você quer saber como organizar o seu dinheiro. '
            '\n   Aperte [2] se você quer fazer um calculo que faz a estimativa da renda.'
            '\n   Aperte [3] se você quer fazer uma estimativa com seu salario?.',8)

    pergunta2 = str(input('\033[40mdigite aqui:\033[m'))
    linha()
    if pergunta2 == '1':
        sleep(0.1)
        dados['salario'] = float(input('\033[35mQuantos você ta recebendo:R$\033[m'))
        linha()
        essencial = dados['salario'] * 0.5
        investimento = 0.3
        gastarE = 0.10
        gastar = 0.10
        l = dados['salario'] * gastarE
        s = dados['salario'] * investimento
        a = dados['salario'] * gastar
        sleep(1)
        escreva('    ORGANIZE SUA VIDA FINANCEIRA!!   ',8)
        sleep(1.5)
        escreva2(f'     ----- METODO PARA O CALCULO -----    ',8)
        linha()
        sleep(1.5)
        escreva2('\33[41mEssenciais     50% - Água, Luz, comida, etc',2)
        sleep(1.5)
        escreva2('\33[44mInvestimenstos 30% - Ativos para libedade financeira e reserva',4)
        sleep(1.5)
        escreva2('\33[46mEducação       10% - Cursos, Livros, Eventos, etc',5)
        sleep(1.5)
        escreva2('\33[43mLazer          10% - Todo que te faça bem (Roupas, Roles, Jogos,etc)',4)
        linha()
        sleep(1.5)
        print(f'\033[40mEm essenciais você terá que gastar: \033[35mR${essencial}\033[m\033[40m')
        sleep(2)
        print(f'\033[40mVocê tem para investir: \033[32mR${s}\033[m\033[40m')
        sleep(2)
        print(f'\033[40mVocê pode gastar com educação até: \033[31mR${a:.1f}\033[m\033[40m')
        sleep(2)
        print(f'\033[40mVocê pode gastar com lazer até: \033[31mR${a:.1f}\033[m\033[40m')
        sleep(2)
        linha()
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
        escreva('Coloque os valores, retabilidade mensal (%) e os meses',8)
        dados.clear()
        sleep(1.0)
        dados['valor inicial '] = float( input('\033[35mValor inicial($):R$\033[m') )
        sleep(1.0)
        dados['rentabilidade mensal '] = float ( input('\033[35mRentabilidade mensal(%):\033[m ') )
        sleep(1.0)
        i = dados['rentabilidade mensal '] / 100
        dados['Meses'] = int( input('\033[35mMeses que vai deixar rendendo:\033[m ') )
        dados['total investido '] = dados['valor inicial '] * (1+i)**dados['Meses']
        composto = dados['valor inicial '] * dados['total investido ']
        list.append(dados.copy())
        linha()
        print(f'\033[40;35mO dinheiro colocado será de \033[31mR${dados["valor inicial "] }')
        print(f'\033[40;35mA rentabilidade mensal será de \033[32m{dados["rentabilidade mensal "]:.0f}%')
        print(f'\033[40;35mNo final do prazo a estimativa é de \033[33mR${dados["total investido "]:.2f} reais')
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


