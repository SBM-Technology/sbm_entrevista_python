from typing import List, Dict, Any
import requests
from flask import current_app
from app import cache


class Taxas:
    """Coleta dados de APIs externas."""

    def __init__(self):
        """Url da API externa de taxas."""
        self.brasil_api_url = current_app.config['BRASILAPI_BASE_URL']
    
    @cache.cached(timeout=300, key_prefix='taxas_brasil')
    def taxas_brasil(self) -> List[Dict[str, Any]]:
        """Coleta taxas de juros da Brasil API."""
        try:
            response = requests.get(f'{self.brasil_api_url}/taxas/v1', timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except requests.RequestException as e:
            current_app.logger.error(f"Erro ao coletar taxas: {e}")
            raise