pedra = 0
papel = 1
tesoura = 2
jogar_novamente = "Sim"
    while (jogar_novamente == "Sim"):
jogador1 = int(input("Jogador1, digite 0 p/pedra, 1 p/papel ou 2/tesoura: " ))
jogador2 = int(input("Jogador2, digite 0 p/pedra, 1 p/papel ou 2/tesoura: " ))
if (0 <= jogador1 <= 2) and (0 <= jogador2 <= 2):
    if (jogador1 == jogador2):
 print("Empate! Ninguém ganhou." ) # empate
e   lif (jogador1 - jogador2) % 3 == 1:
 print("Jogador 1 ganhou." )
else:
 print("Jogador 2 ganhou." )
else:
print("Opção inválida." )
jogar_novamente = input("Você quer tentar novamente? Digite Sim ou Não" )
print("Até a próxima!" )