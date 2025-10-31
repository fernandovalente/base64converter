# Base64Converter

Uma ferramenta Python pythônica e intuitiva para conversão bidirecional entre arquivos e representação base64.

## 📋 Descrição

O `Base64Converter` é uma classe Python que simplifica a conversão entre arquivos binários e suas representações em base64. Ideal para situações onde você precisa codificar arquivos para transmissão via APIs, armazenamento em bancos de dados, ou qualquer outra necessidade de representação base64.

## ✨ Características

- **Interface Simples**: Métodos `converter()` e `desconverter()` para operações diretas
- **Código Pythônico**: Implementado seguindo as melhores práticas do Python
- **Type Hints**: Anotações de tipo completas para melhor experiência de desenvolvimento
- **Tratamento de Erros**: Validações e mensagens de erro claras
- **Flexível**: Aceita caminhos como string ou objetos `Path`
- **Sem Dependências Externas**: Utiliza apenas a biblioteca padrão do Python
- **Criação Automática de Diretórios**: Cria diretórios automaticamente ao salvar arquivos

## 🔧 Requisitos

- Python 3.6 ou superior

## 📦 Instalação

Este projeto não requer instalação de pacotes externos. Basta ter Python instalado e usar o arquivo `base64_converter.py`.

Para instalar dependências opcionais (se houver):

```bash
pip install -r requirements.txt
```

## 🚀 Uso Básico

### Exemplo 1: Conversão Simples

```python
from base64_converter import Base64Converter

# Criar instância do conversor
converter = Base64Converter()

# Converter arquivo para base64
base64_string = converter.converter("imagem.jpg")
print(f"Base64: {base64_string[:50]}...")

# Converter base64 de volta para arquivo
converter.desconverter("imagem_copia.jpg")
```

### Exemplo 2: Usando Properties

```python
from base64_converter import Base64Converter

converter = Base64Converter()

# Converter arquivo
base64_str = converter.converter("documento.pdf")

# Acessar o base64 armazenado
print(converter.base64_string)

# Desconverter em outro local
converter.desconverter("backup/documento_copia.pdf")
```

### Exemplo 3: Inicialização com Valores

```python
from base64_converter import Base64Converter

# Inicializar com base64 já existente
base64_existente = "SGVsbG8gV29ybGQh"
converter = Base64Converter(base64_string=base64_existente)

# Desconverter diretamente
converter.desconverter("saida.txt")
```

## 📚 Documentação da API

### Classe `Base64Converter`

#### Construtor

```python
Base64Converter(base64_string: Optional[str] = None, arquivo_path: Optional[Union[str, Path]] = None)
```

Inicializa o conversor com valores opcionais.

**Parâmetros:**
- `base64_string` (opcional): String base64 para inicializar
- `arquivo_path` (opcional): Caminho do arquivo para inicializar

#### Métodos Principais

##### `converter(arquivo_path: Union[str, Path]) -> str`

Converte um arquivo para representação base64.

**Parâmetros:**
- `arquivo_path`: Caminho do arquivo a ser convertido

**Retorna:**
- `str`: String base64 do conteúdo do arquivo

**Exceções:**
- `FileNotFoundError`: Se o arquivo não existir
- `ValueError`: Se o caminho fornecido não for válido

**Exemplo:**
```python
base64_str = converter.converter("arquivo.pdf")
```

##### `desconverter(arquivo_path: Union[str, Path]) -> Path`

Converte uma string base64 (armazenada internamente) para arquivo.

**Parâmetros:**
- `arquivo_path`: Caminho onde salvar o arquivo decodificado

**Retorna:**
- `Path`: Caminho do arquivo criado

**Exceções:**
- `ValueError`: Se não houver base64 armazenado ou se o caminho for inválido

**Exemplo:**
```python
converter.desconverter("saida.pdf")
```

#### Métodos Auxiliares

##### `arquivo_para_base64(arquivo_path: Optional[Union[str, Path]] = None) -> str`

Método mais verboso para converter arquivo para base64. Se `arquivo_path` não for fornecido, usa `self.arquivo_path`.

##### `base64_para_arquivo(base64_string: Optional[str] = None, arquivo_path: Optional[Union[str, Path]] = None) -> Path`

Método mais verboso para converter base64 para arquivo. Permite especificar ambos os parâmetros diretamente.

#### Properties

##### `base64_string: Optional[str]`

Getter/Setter para a string base64 atual.

##### `arquivo_path: Optional[Path]`

Getter/Setter para o caminho do arquivo atual.

## 💡 Exemplos Práticos

### Exemplo 1: Converter Imagem para Base64 e Enviar via API

```python
from base64_converter import Base64Converter

converter = Base64Converter()
base64_image = converter.converter("foto.jpg")

# Enviar base64_image via API
# api.send_image(base64_image)
```

### Exemplo 2: Receber Base64 e Salvar como Arquivo

```python
from base64_converter import Base64Converter

# Receber base64 de uma API
base64_recebido = "iVBORw0KGgoAAAANSUhEUgAA..."

converter = Base64Converter(base64_string=base64_recebido)
converter.desconverter("imagem_recebida.png")
```

### Exemplo 3: Processamento em Lote

```python
from base64_converter import Base64Converter
from pathlib import Path

converter = Base64Converter()

# Converter múltiplos arquivos
arquivos = ["arquivo1.pdf", "arquivo2.pdf", "arquivo3.pdf"]
base64_list = []

for arquivo in arquivos:
    base64_str = converter.converter(arquivo)
    base64_list.append(base64_str)
    print(f"{arquivo} convertido: {len(base64_str)} caracteres")
```

### Exemplo 4: Validação e Tratamento de Erros

```python
from base64_converter import Base64Converter
from pathlib import Path

converter = Base64Converter()

try:
    base64_str = converter.converter("arquivo_inexistente.txt")
except FileNotFoundError as e:
    print(f"Erro: {e}")
except ValueError as e:
    print(f"Erro de validação: {e}")

try:
    converter.desconverter("saida.txt")
except ValueError as e:
    print(f"Erro: {e}")  # Não há base64 armazenado
```

## 🏗️ Estrutura do Projeto

```
base64converter/
├── base64_converter.py  # Classe principal
├── requirements.txt      # Dependências (apenas módulos padrão)
└── README.md            # Este arquivo
```

## 🔍 Tratamento de Erros

A classe `Base64Converter` levanta as seguintes exceções:

- **`FileNotFoundError`**: Quando o arquivo especificado não existe
- **`ValueError`**: Quando:
  - Nenhum caminho de arquivo é fornecido
  - O caminho não é um arquivo válido
  - String base64 é inválida
  - Tentativa de desconverter sem base64 armazenado
- **`TypeError`**: Quando o tipo de dado fornecido é incorreto (ex: base64_string não é string)

## 📝 Notas

- A classe armazena internamente o último base64 convertido, permitindo reutilização
- Diretórios são criados automaticamente ao salvar arquivos em caminhos não existentes
- A classe trabalha com qualquer tipo de arquivo binário (imagens, PDFs, vídeos, etc.)

## 🤝 Contribuindo

Este é um projeto simples e direto. Sinta-se à vontade para fazer fork, melhorar e adaptar conforme suas necessidades.

## 📄 Licença

Este projeto está disponível para uso livre.
