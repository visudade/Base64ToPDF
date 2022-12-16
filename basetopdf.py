# Importando função b64decode do modulo base64 e a biblioteca python-virustotal
try:
    from base64 import b64decode
    import virustotal
except ImportError:
    print("O módulo base64 ou a biblioteca python-virustotal não estão instalados. Por favor, instale-os antes de continuar.")
    exit()

# Pedindo o nome do arquivo de entrada para o usuário
nome_arquivo = input("Insira o nome do arquivo de entrada: ")

# Verificando se o nome do arquivo tem a extensão .txt
if not nome_arquivo.endswith('.txt'):
    raise ValueError("O arquivo de entrada deve ser um arquivo .txt.")

# Tentando abrir o arquivo em modo de leitura
try:
    with open(nome_arquivo, 'r') as f:
        # Lendo o conteúdo do arquivo
        b64 = f.read()
except FileNotFoundError:
    print("O arquivo de entrada não foi encontrado. Por favor, verifique se o nome do arquivo está correto e se o arquivo está no mesmo diretório do código.")
    exit()

# Verificando se a string de base64 é válida
if len(b64) % 4 != 0:
    raise ValueError("A string de base64 não é um tamanho múltiplo de 4.")

if not all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" for c in b64):
    raise ValueError("A string de base64 contém caracteres inválidos.")

# Decodificando a string de base64
bytes = b64decode(b64)

# Verificando se os primeiros bytes da string decodificada são a assinatura do arquivo PDF
if bytes[0:4] != b'%PDF':
  raise ValueError('Missing the PDF file signature')

# Criando um objeto VirusTotalAPI
vt = virustotal.VirusTotal("SUA CHAVE API AQUI")

# Verificando o arquivo PDF decodificado com a VirusTotal
try:
    resultado = vt.file_scan(bytes)
except virustotal.VirusTotalError as e:
    print("Ocorreu um erro ao verificar o arquivo com a VirusTotal:", e)
    exit()

if resultado.positives == 0:
    print("O arquivo não foi detectado como vírus pela VirusTotal.")
else:
    print("O arquivo foi detectado como vírus pela VirusTotal. Por favor, não prossiga.")
    exit()

# Tentando abrir o arquivo PDF decodificado com a biblioteca PyPDF2
try:
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(bytes)
except ImportError:
    print("A biblioteca PyPDF2 não está instalada. Por favor, instale-a antes de continuar.")
    exit()
except PyPDF2.utils.PdfReadError:
    raise ValueError("A string de base64 não é um arquivo PDF válido.")

# Pedindo o nome do arquivo de saída para o usuário
nome_arquivo = input("Insira o nome do arquivo de saída: ")

# Verificando se o arquivo de saída já existe
if os.path.exists(nome_arquivo):
    raise ValueError("O arquivo de saída já existe. Por favor, escolha outro nome de arquivo ou mova o arquivo existente para outro local.")
    if sobrescrever != 's':
        print("
