# Recebe os valores do usuário
nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura * altura)

# Estrutura de decisão que retorna o imc do usuário
if imc < 17:
    print("{}, você se encontra muito abaixo do peso".format(nome))
elif imc > 16 and imc <= 18.49:
    print("{}, você se encontra abaixo do peso".format(nome))
elif imc >= 18.50 and  imc < 25:
    print("{}, você se encontra com o peso normal".format(nome))
elif imc >= 25 and imc < 30:
    print("{}, você se encontra acima do peso".format(nome))
elif imc >= 30 and imc < 35:
    print("{}, você se encontra no estagio de obesidade I".format(nome))
elif imc >= 35 and imc < 40:
    print("{}, você se encontra no estagio de obesidade II (severa)".format(nome))
elif imc > 40:
    print("{}, você se encontra no estagio de obesidade III (mórbida)".format(nome))