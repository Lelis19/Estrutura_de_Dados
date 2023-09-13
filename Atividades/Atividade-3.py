import math

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def verificar_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

def calcular_soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    count = 0
    for char in texto:
        if char in vogais:
            count += 1
    return count

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def converter_temperatura(valor, escala):
    if escala == 'C':
        return (valor * 9/5) + 32
    elif escala == 'F':
        return (valor - 32) * 5/9

def gerar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    return fibonacci

while True:
    print("\nEscolha uma opção:")
    print("1. Calcular média de notas e verificar aprovação")
    print("2. Calcular fatorial de um número")
    print("3. Verificar se uma palavra/frase é um palíndromo")
    print("4. Calcular a soma dos dígitos de um número")
    print("5. Verificar se um número é primo")
    print("6. Contar vogais em uma string")
    print("7. Calcular IMC")
    print("8. Converter temperatura")
    print("9. Calculadora (+, -, *, /)")
    print("10. Gerar sequência de Fibonacci")
    print("0. Sair")

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        notas = []
        for i in range(5):
            nota = float(input("Digite a {}ª nota: ".format(i+1)))
            notas.append(nota)
        media = calcular_media(notas)
        resultado = verificar_aprovacao(media)
        print("Média:", media)
        print("Situação:", resultado)
    elif escolha == 2:
        numero = int(input("Digite um número inteiro positivo: "))
        resultado = calcular_fatorial(numero)
        print("Fatorial:", resultado)
    elif escolha == 3:
        texto = input("Digite uma palavra ou frase: ")
        resultado = verificar_palindromo(texto)
        if resultado:
            print("É um palíndromo.")
        else:
            print("Não é um palíndromo.")
    elif escolha == 4:
        numero = int(input("Digite um número inteiro positivo: "))
        resultado = calcular_soma_digitos(numero)
        print("Soma dos dígitos:", resultado)
    elif escolha == 5:
        numero = int(input("Digite um número inteiro positivo: "))
        resultado = verificar_primo(numero)
        if resultado:
            print("É primo.")
        else:
            print("Não é primo.")
    elif escolha == 6:
        texto = input("Digite uma string: ")
        resultado = contar_vogais(texto)
        print("Número de vogais:", resultado)
    elif escolha == 7:
        peso = float(input("Digite o peso (kg): "))
        altura = float(input("Digite a altura (m): "))
        resultado = calcular_imc(peso, altura)
        print("IMC:", resultado)
    elif escolha == 8:
        valor = float(input("Digite o valor da temperatura: "))
        escala = input("Digite a escala (C para Celsius, F para Fahrenheit): ")
        resultado = converter_temperatura(valor, escala)
        print("Resultado:", resultado)
    elif escolha == 9:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Não é possível dividir por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            continue
        print("Resultado:", resultado)
    elif escolha == 10:
        n = int(input("Digite o número de termos da sequência de Fibonacci: "))
        resultado = gerar_fibonacci(n)
        print("Sequência de Fibonacci:", resultado)
    elif escolha == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
