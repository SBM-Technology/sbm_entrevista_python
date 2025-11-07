"""
Serviço de coleta de dados de APIs externas.
"""
import requests
from datetime import datetime
from flask import current_app
from app import db, cache
from app.models import Cotacao


class DataCollector:
    """Coleta dados de APIs externas."""

    def __init__(self):
        self.awesome_api_url = current_app.config['AWESOMEAPI_BASE_URL']
        self.brasil_api_url = current_app.config['BRASILAPI_BASE_URL']
    
    @cache.cached(timeout=300, key_prefix='cotacoes_usd_brl')
    def coletar_cotacoes(self) -> int:
        """
        Coleta cotações de moedas da AwesomeAPI.
        
        Returns:
            int: Número de cotações coletadas
        """
        
        try:
            # Coleta USD-BRL e EUR-BRL
            response = requests.get(f'{self.awesome_api_url}/last/USD-BRL,EUR-BRL', timeout=10)
            response.raise_for_status()
            
            dados = response.json()
            num_cotacoes = self._processa_salva_cotacao(dados)
            return num_cotacoes
            
        except requests.RequestException as e:
            current_app.logger.error(f"Erro ao coletar cotações: {e}")
            raise
    
    def coletar_historico_cotacoes(self, moeda='USD', dias=30) -> list[Cotacao]:
        """
        Coleta histórico de cotações.
        
        Args:
            moeda: Código da moeda (USD, EUR)
            dias: Número de dias de histórico
            
        Returns:
            list: Lista de cotações históricas
        """
        
        try:
            response = requests.get(
                f'{self.awesome_api_url}/json/daily/{moeda}-BRL/{dias}',
                timeout=10
            )
            response.raise_for_status()
            
            dados = response.json()
            cotacoes = []
            
            for item in dados:
                cotacao = Cotacao(
                    moeda=moeda,
                    valor=float(item['bid']),
                    data_hora=datetime.fromtimestamp(int(item['timestamp']))
                )

                if not self._existe_cotacao(cotacao):
                    cotacoes.append(cotacao)
                    db.session.add(cotacao)
            
            db.session.commit()
            return cotacoes
            
        except requests.RequestException as e:
            current_app.logger.error(f"Erro ao coletar histórico: {e}")
            raise
    
    @cache.cached(timeout=3600, key_prefix='taxas_brasil')
    def coletar_taxas_brasil(self) -> list[dict[str, any]]:
        """
        Coleta taxas de juros da Brasil API.
        
        Returns:
            dict: Dados das taxas
        """
        try:
            response = requests.get(f'{self.brasil_api_url}/taxas/v1', timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except requests.RequestException as e:
            current_app.logger.error(f"Erro ao coletar taxas: {e}")
            raise

    def _existe_cotacao(cotacao: Cotacao) -> bool:
        return Cotacao.query.filter_by(
            moeda=cotacao.moeda,
            data_hora=cotacao.data_hora
        ).first() is not None
    
    def _processa_salva_cotacao(self, dados: dict[str, any]) -> int:
        num_cotacoes = 0
            
        # Processa USD
        if 'USDBRL' in dados:
            usd_data = dados['USDBRL']
            cotacao = Cotacao(
                moeda='USD',
                valor=float(usd_data['bid']),
                data_hora=datetime.fromtimestamp(int(usd_data['timestamp']))
            )
            db.session.add(cotacao)
            num_cotacoes += 1
        
        # Processa EUR
        if 'EURBRL' in dados:
            eur_data = dados['EURBRL']
            cotacao = Cotacao(
                moeda='EUR',
                valor=float(eur_data['bid']),
                data_hora=datetime.fromtimestamp(int(eur_data['timestamp']))
            )
            db.session.add(cotacao)
            num_cotacoes += 1
        
        db.session.commit()
        return num_cotacoes