# --- Declaração de Variáveis + Input para entrada de dados ---

nota1 = float (input ("Digite a 1ª Nota do Aluno: "))
nota2 = float (input ("Digite a 2ª Nota do Aluno: "))
nota3 = float (input ("Digite a 3ª Nota do Aluno: "))

# --- Declaração de variável para soma + formula de calculo ---
#obs declara-se (nota1 + nota2 + nota3) entre parenteses para o sistema primeiro somar, para depois dividir.
media = (nota1 + nota2 + nota3) / 3


  # --- Comando para impressão na tela ---
# obs: .format (nota1, nota2, nota3, media) preenche os campos {} com as váriaveis declaradas
# para usar mais casas decimais depois do ponto usa-se {:.2f} ou {:.1f}

print ("\n A Média entre {}, {} e {} é: {}" .format(nota1, nota2, nota3, media))

        # --- estrutura de condição ---

if media > 5: 
  print ("\n Aprovado: Sua nota é Maior do que a minima de 5")
elif media == 5: 
  print ("\n Aprovado: Sua nota esta na media minima")
else: 
  print ("\n Reprovado: Você não atingiu a media minima de 5")

