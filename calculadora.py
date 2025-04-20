def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Não é possível calcular raiz de número negativo!"
    return a ** 0.5

def calculadora():
    print("\n=== Calculadora Python ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Sair")

    while True:
        try:
            opcao = int(input("\nEscolha uma operação (1-7): "))
            
            if opcao == 7:
                print("Obrigado por usar a calculadora!")
                break
                
            if opcao == 6:
                num = float(input("Digite um número: "))
                resultado = raiz_quadrada(num)
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == 1:
                    resultado = soma(num1, num2)
                elif opcao == 2:
                    resultado = subtracao(num1, num2)
                elif opcao == 3:
                    resultado = multiplicacao(num1, num2)
                elif opcao == 4:
                    resultado = divisao(num1, num2)
                elif opcao == 5:
                    resultado = potencia(num1, num2)
                else:
                    print("Opção inválida!")
                    continue
            
            print(f"\nResultado: {resultado}")
            
        except ValueError:
            print("Erro: Por favor, digite apenas números!")
        except Exception as e:
            print(f"Erro: {str(e)}")

if __name__ == "__main__":
    calculadora()