def executar_quiz(perguntas):
   pontuacao = 0


   for pergunta in perguntas:
       print(pergunta["pergunta"])
       for i, opcao in enumerate(pergunta["opcoes"], start=1):
           print(f"{i}. {opcao}")
      
       resposta_usuario = input("Escolha a opção correta (1-4): ")
      
       if resposta_usuario.isdigit() and 1 <= int(resposta_usuario) <= 4:
           resposta_usuario = int(resposta_usuario) - 1
           if pergunta["opcoes"][resposta_usuario] == pergunta["resposta"]:
               print("Correto!\n")
               pontuacao += 1
           else:
               print(f"Incorreto! A resposta correta é: {pergunta['resposta']}\n")
       else:
           print("Opção inválida. Por favor, escolha um número entre 1 e 4.\n")


   print(f"Sua pontuação final é: {pontuacao} de {len(perguntas)}")