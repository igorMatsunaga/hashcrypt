#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Code: IgorMatsunaga - NSW
#Site: https://nsworld.com.br
#Github: https://github.com.br/igorMatsunaga

import bcrypt
import time

logo = '''
██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
███████║███████║███████╗███████║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║   ██║   ██║        ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝                                                                   
'''
print('\033[33m' + logo)
# Caso deseje inserir uma palavra-chave fixa, use o prefixo 'b' para criar uma string de byte
#password = b"palavra-chave"

#Para receber uma entradade um usuário utilize o método .encode("utf-8")
password = input("Digite a palavra-chave a ser cifrada: ").encode("utf-8")

#Gerando tempo e resultados
inicio = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
fim = time.time()

# Subtração do tempo final com tempo de inicio
t = fim - inicio

print("\nO resultado é: ")
print(hashed)
print("\nO tempo gasto foi:")
print(t)