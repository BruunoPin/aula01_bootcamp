
# O programa deve começar solicitando ao usuário que insira seu nome.
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000"
try:
    nome = input("Digite seu nome: ")

    if not nome:
        raise ValueError("Nome não pode ser vazio.")
    if not nome.replace(' ', '').isalpha():
        raise ValueError("Nome deve conter apenas letras.")
    else:
        print(f'Nome valido: {nome}')

    salario = float(input("Digite seu salário: "))
    if salario < 0:
        raise ValueError("Salário não pode ser negativo.")
    else:
        print(f'Salario valido: {salario}')

    bonus = float(input("Quanto de bônus: "))
    if bonus < 0:
        raise ValueError("Bônus não pode ser negativo.")
    else:
        print(f'Bônus valido: {bonus}')

    bonus_final = bonus * 1.2
    kpi = (salario * bonus_final) / 1000

    print(f"Seu KPI é: {kpi:.2f}")
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")
    
except ValueError as e:
    print(f'Erro: {e}')



