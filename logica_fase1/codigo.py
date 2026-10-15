# #### 4. Cadastro de e-mails
# A empresa sempre se comunica com seus clientes por email. Para isso, a gente tem em cada página um cadastro de nome e e-mail. 
# Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail valido, 
# verificando se tem '@' e se depois do '@' tem algum ponto. Afinal:

# - fulanogmail.com não é um e-mail válido
# - fulano@gmail não é um e-mail válido
# - fulano@gmail.com é um e-mail válido

# Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
# 1. Se o nome e e-mail foram preenchidos, caso contrario ele deve avisar para preencher todos os dados corretamente
# 2. Se o e-mail contém '@' e se depois do '@' existe algum '.' caso contrario ele deve exibir uma mensagem de e-mail inválido

# Obs.: Pode te ajudar lembrar o método  .find() da aula de métodos de String. 
# Você pode testar o que ele da como resposta caso ele não encontre um item dentro da strings.

print('Cadastrar novo login')
nome = input('Informe seu Nome: ')
email = input('Informe seu E-mail: ')



if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluido')
    else:
        print('E-mail invalido')
else:
    print('Digite o nome e e-mail corretamente!')