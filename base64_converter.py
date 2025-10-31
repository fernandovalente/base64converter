"""
Módulo para conversão entre arquivos e representação base64.
"""

import base64
from pathlib import Path
from typing import Union, Optional


class Base64Converter:
    """
    Classe para converter arquivos em base64 e vice-versa.
    
    Exemplo de uso:
        # Converter arquivo para base64
        converter = Base64Converter()
        base64_str = converter.converter("imagem.jpg")
        
        # Converter base64 para arquivo
        converter.desconverter("imagem_copia.jpg")
    """
    
    def __init__(self, base64_string: Optional[str] = None, arquivo_path: Optional[Union[str, Path]] = None):
        """
        Inicializa o conversor.
        
        Args:
            base64_string: String base64 opcional para inicializar
            arquivo_path: Caminho do arquivo opcional para inicializar
        """
        self._base64_string = base64_string
        self._arquivo_path = Path(arquivo_path) if arquivo_path else None
    
    @property
    def base64_string(self) -> Optional[str]:
        """Retorna a string base64 atual."""
        return self._base64_string
    
    @base64_string.setter
    def base64_string(self, value: str):
        """Define a string base64."""
        if not isinstance(value, str):
            raise TypeError("base64_string deve ser uma string")
        self._base64_string = value
    
    @property
    def arquivo_path(self) -> Optional[Path]:
        """Retorna o caminho do arquivo atual."""
        return self._arquivo_path
    
    @arquivo_path.setter
    def arquivo_path(self, value: Union[str, Path]):
        """Define o caminho do arquivo."""
        self._arquivo_path = Path(value)
    
    def arquivo_para_base64(self, arquivo_path: Optional[Union[str, Path]] = None) -> str:
        """
        Converte um arquivo para representação base64.
        
        Args:
            arquivo_path: Caminho do arquivo. Se None, usa self.arquivo_path
            
        Returns:
            String base64 do conteúdo do arquivo
            
        Raises:
            FileNotFoundError: Se o arquivo não existir
            ValueError: Se nenhum caminho de arquivo for fornecido
        """
        path = Path(arquivo_path) if arquivo_path else self._arquivo_path
        
        if path is None:
            raise ValueError("É necessário fornecer um caminho de arquivo")
        
        if not path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {path}")
        
        if not path.is_file():
            raise ValueError(f"O caminho não é um arquivo: {path}")
        
        with open(path, 'rb') as arquivo:
            conteudo = arquivo.read()
            base64_encoded = base64.b64encode(conteudo).decode('utf-8')
            self._base64_string = base64_encoded
            return base64_encoded
    
    def base64_para_arquivo(
        self, 
        base64_string: Optional[str] = None, 
        arquivo_path: Optional[Union[str, Path]] = None
    ) -> Path:
        """
        Converte uma string base64 para arquivo.
        
        Args:
            base64_string: String base64. Se None, usa self.base64_string
            arquivo_path: Caminho onde salvar o arquivo. Se None, usa self.arquivo_path
            
        Returns:
            Path do arquivo criado
            
        Raises:
            ValueError: Se base64_string ou arquivo_path não forem fornecidos
            base64.binascii.Error: Se a string base64 for inválida
        """
        base64_str = base64_string if base64_string is not None else self._base64_string
        path = Path(arquivo_path) if arquivo_path else self._arquivo_path
        
        if base64_str is None:
            raise ValueError("É necessário fornecer uma string base64")
        
        if path is None:
            raise ValueError("É necessário fornecer um caminho para salvar o arquivo")
        
        try:
            conteudo_decodificado = base64.b64decode(base64_str)
        except Exception as e:
            raise ValueError(f"String base64 inválida: {e}") from e
        
        # Cria diretórios se necessário
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'wb') as arquivo:
            arquivo.write(conteudo_decodificado)
        
        self._arquivo_path = path
        return path
    
    def converter(self, arquivo_path: Union[str, Path]) -> str:
        """
        Alias pythônico para arquivo_para_base64.
        
        Args:
            arquivo_path: Caminho do arquivo a ser convertido
            
        Returns:
            String base64
        """
        return self.arquivo_para_base64(arquivo_path)
    
    def desconverter(self, arquivo_path: Union[str, Path]) -> Path:
        """
        Alias pythônico para base64_para_arquivo.
        
        Args:
            arquivo_path: Caminho onde salvar o arquivo decodificado
            
        Returns:
            Path do arquivo criado
        """
        if self._base64_string is None:
            raise ValueError("É necessário ter uma string base64. Use converter() primeiro ou forneça base64_string.")
        return self.base64_para_arquivo(arquivo_path=arquivo_path)
    
    def __str__(self) -> str:
        """Representação em string do objeto."""
        status = []
        if self._base64_string:
            status.append(f"base64: {len(self._base64_string)} caracteres")
        if self._arquivo_path:
            status.append(f"arquivo: {self._arquivo_path}")
        return f"Base64Converter({', '.join(status) if status else 'vazio'})"
    
    def __repr__(self) -> str:
        """Representação oficial do objeto."""
        return f"Base64Converter(base64_string={'...' if self._base64_string else None}, arquivo_path={self._arquivo_path})"

