# hashcrypt
<!-- wp:tadv/classic-paragraph -->
<p>Script para criação de hash para palavras-chave, utilizando Python(bcrypt)</p>
<p>Hash de senha em Python com Bcrypt</p>
<p>O que é hashing?</p>
<p>Para não ser confundido com criptografia, hash é o processo irrevogável e unidirecional de pegar uma string e se transformar em um tamanho fixo de caracteres aparentemente aleatórios. Por exemplo, aqui está a palavra meuhash  usando bcrypt:</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'$2b$12$hkotUkSeOhtlV2CUxHfLyuCtWBNTvg6KrkZk/hOKfyORJFgiHFieK'</code></pre>
<!-- /wp:code -->

<!-- wp:tadv/classic-paragraph -->
<p>Ao contrário da criptografia, que pode ser decodificada e revertida em sua forma original, o hashing é irreversível, ou seja, não há como recuperar a string original, tornando-a ideal para senhas e autenticação. Comparando Senhas Se executarmos a mesma bcrypt função de hashing novamente na mesma palavra meuhash, obteremos: </p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'$2b$12$aOCSI6vtMZYtB7me4CK2bO1M1R1I.l5mvahmffvsguzucZk3E9j3.'</code></pre>
<!-- /wp:code -->

<!-- wp:tadv/classic-paragraph -->
<p>O que é claramente diferente do nosso primeiro hash ... Se você não está familiarizado com hashing, você pode estar pensando neste ponto "Então, como eu comparo uma senha com uma senha com hash ?, especialmente quando elas são totalmente diferentes" ... a única forma será através de um ataque de força bruta. Instalando o hashcrack</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install –r requeriments.txt Utilizar o hashcrack

python3 hashCrypt.py</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":3003} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/hashCrypt.png" alt="" class="wp-image-3003"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p>Digite a palavra-chave e o script se encarregará do resto.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3004} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/hashTeste.png" alt="" class="wp-image-3004"/></figure>
<!-- /wp:image -->

