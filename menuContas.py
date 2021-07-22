n1 = int(input("Fale o 1° valor: "))
n2 = int(input("Fale o 2° valor: "))
opcao = 0
while opcao != 5:
  print('''\n[1]SOMA
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NUMEROS
[5]SAIR DO PROGAMA\n''')
  opcao = int(input(">>>>>> ESCOLHA UMA OPÇÃO: "))
  if opcao == 1:
    #esse f significa formatado o mesmo de usar o .format
    print(f"\nA soma de {n1} + {n2} = {n1+n2}")
  elif opcao == 2:
    print(f"\nA multiplicação de {n1} x {n2} = {n1*n2}")
  elif opcao == 3:
    if n1 > n2:
      maior = n1
      menor = n2
    elif n2 > n1:
      maior = n2
      menor = n1
    print(f"{maior} é maior que {menor}")
  elif opcao == 4:
    n1 = int(input("Digite o 1° novo valor: "))
    n2 = int(input("Digite o 2° novo valor: "))
  elif opcao == 5:
    print("SAINDO...")
  else:
    print("Opção invalida!")
