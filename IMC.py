print(" == Sistema para calcular IMC == \nIndique sua altura e peso: ")
altura = float(input("Altura(m): "))
peso = float(input("Peso(kg): "))
 
resul = peso/(altura*altura)
 
if resul < 18.5:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é abaixo do peso")
elif resul < 24.9:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é peso normal")
elif resul < 29.9:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é Sobrepeso")
elif resul < 39.9:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é Obesidade")
else:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é Obesidade Grave")
 

 