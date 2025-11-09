from typing import Dict, List, Any
from app.models import Cotacao
from .cotacoes import Cotacoes
from .taxas import Taxas


class DataCollector:

    def __init__(self, cotacoes: Cotacoes | None = None, taxas: Taxas | None = None):
        """Serviços de coleta de dados de APIs externas."""
        self.cotacoes = cotacoes or Cotacoes()
        self.taxas = taxas or Taxas()
    
    def coletar_cotacoes(self) -> int:
        """
        Coleta cotações de moedas da AwesomeAPI.
        
        Returns:
            int: Número de cotações coletadas
        """
        return self.cotacoes.cotacoes()

    def coletar_historico_cotacoes(self, moeda: str='USD', dias: int=30) -> List[Cotacao]:
        """
        Coleta histórico de cotações.
        
        Args:
            moeda: Código da moeda (USD, EUR)
            dias: Número de dias de histórico
            
        Returns:
            list: Lista de cotações históricas
        """
        return self.cotacoes.historico_cotacoes(moeda, dias)
    
    def coletar_taxas_brasil(self) -> List[Dict[str, Any]]:
        """
        Coleta taxas de juros da Brasil API.
        
        Returns:
            dict: Dados das taxas
        """
        return self.taxas.taxas_brasil()