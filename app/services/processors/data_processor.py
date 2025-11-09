from werkzeug.datastructures import FileStorage
from .csv_processor import CsvProcessor


class DataProcessor:
    """Processa e valida dados."""

    def __init__(self, csv_processor: CsvProcessor | None = None):
        self.csv_processor = csv_processor or CsvProcessor()
    
    def processar_upload(self, file: FileStorage, tipo: str) -> int:
        """
        Processa arquivo enviado via upload.
        
        Args:
            file: Arquivo FileStorage do Flask
            tipo: Tipo de dados (vendas, custos)
            
        Returns:
            int: Número de registros processados
        """
        return self.csv_processor.processar_vendas_custos(file, tipo)