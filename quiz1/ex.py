# Problema 1
# Rolien e Naej são os desenvolvedores de um grande portal de programação.
# Para ajudar no novo sistema de cadastro do site, eles requisitaram a sua ajuda.
# Seu trabalho é fazer um código que valide as senhas que são cadastradas no portal,
# para isso você deve atentar aos requisitos a seguir:
# A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
# A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
# Além disso, a senha pode ter de 6 a 32 caracteres.

# Entrada
# A entrada contém vários casos de teste e termina com final de arquivo. Cada linha tem uma string S, correspondente a senha que é inserida pelo usuário no momento do cadastro.

# Saída
# A saída contém uma linha, que pode ser “Senha valida.”, caso a senha tenha cada item dos requisitos solicitados anteriormente, ou “Senha invalida.”, se um ou mais requisitos não forem atendidos.


import re


def validate_password(s):
    if len(s) < 6 or len(s) > 32:
        return False

    # Check if there is at least one uppercase letter, one lowercase letter, and one digit
    if not re.search("[A-Z]", s) or not re.search("[a-z]", s) or not re.search("[0-9]", s):
        return False

    # Check if the password contains only alphanumeric characters
    if not s.isalnum():
        return False

    return True


print("Enter the password: ")
while True:
    try:
        password = input()
        if validate_password(password):
            print("Valid password.")
        else:
            print("Invalid password.")
    except EOFError:
        print("Invalid password.")
