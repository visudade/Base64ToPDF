# Importando função b64decode do modulo base64 - Lembrar de instalar modulo antes de rodar
from base64 import b64decode

# Ponto de inserção do Base64 que deve ser decodado
b64 = 'XXXX BASE64 XXXXX'

# Validando caracteres do Base64
bytes = b64decode(b64, validate=True)

# Validando se o Base64 inserido é de fato um Arquivo PDF
# Evitar utilizar fontes não confiaveis pois esta não é uma validação segura
if bytes[0:4] != b'%PDF':
  raise ValueError('Missing the PDF file signature')

# Escrevendo arquivo
f = open('arquivo.pdf', 'wb')
f.write(bytes)
f.close()
