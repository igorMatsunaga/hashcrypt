# hashcrypt
Script para criação de hash para palavras-chave, utilizando Python(bcrypt)

Hash de senha em Python com Bcrypt
O que é hashing

Para não ser confundido com criptografia, hash é o processo irrevogável e unidirecional de pegar uma string e se transformar em um tamanho fixo de caracteres aparentemente aleatórios.
Por exemplo, aqui está a palavra meuhash hash usando bcrypt:
b'$2b$12$hkotUkSeOhtlV2CUxHfLyuCtWBNTvg6KrkZk/hOKfyORJFgiHFieK'

Ao contrário da criptografia, que pode ser decodificada e revertida em sua forma original, o hashing é irreversível, ou seja, não há como recuperar a string original, tornando-a ideal para senhas e autenticação.
Comparando Senhas
Se executarmos a mesma bcrypt função de hashing novamente na mesma palavra meuhash, obteremos:
b'$2b$12$aOCSI6vtMZYtB7me4CK2bO1M1R1I.l5mvahmffvsguzucZk3E9j3.'
O que é claramente diferente do nosso primeiro hash ... 
Se você não está familiarizado com hashing, você pode estar pensando neste ponto "Então, como eu comparo uma senha com uma senha com hash ?, especialmente quando elas são totalmente diferentes" ... a única forma será através de um ataque de força bruta.
Instalando o hashcrack

pip install –r requeriments.txt
Utilizar o hashcrack

python hashCrypt.py

Digite a palavra-chave e o script se encarregará do resto.  

