from typing import Dict, Any
from .margem import Margem
from .sazonalidade import Sazonalidade
from .categoria import Categoria
from .regiao import Regiao
from .series import Series
from .vendedor import Vendedor


class Analytics:
    """
    Serviço de análises e agregações.
    """
    def __init__(
        self, margem: Margem | None = None,
        sazonalidade: Sazonalidade | None = None,
        categoria: Categoria | None = None,
        regiao: Regiao | None = None,
        series: Series | None = None,
        vendedor: Vendedor | None = None
    ):
        self.margem = margem or Margem()
        self.sazonalidade = sazonalidade or Sazonalidade()
        self.categoria = categoria or Categoria()
        self.regiao = regiao or Regiao()
        self.series = series or Series()
        self.vendedor = vendedor or Vendedor()


    """Realiza análises estatísticas e agregações."""
    
    def calcular_kpis(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """
        Calcula KPIs principais.
        
        Args:
            data_inicio: Data inicial (string YYYY-MM-DD)
            data_fim: Data final (string YYYY-MM-DD)
            
        Returns:
            dict: KPIs calculados
        """

        return self.series.calcular_kpis(data_inicio, data_fim)
    
    def vendas_ao_longo_tempo(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """
        Retorna série temporal de vendas.
        
        Returns:
            dict: Dados para gráfico de linhas
        """

        return self.series.calcular_vendas_ao_longo_tempo(data_inicio, data_fim)
    
    def vendas_por_categoria(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """
        Retorna vendas agregadas por categoria.
        
        Returns:
            dict: Dados para gráfico de barras
        """

        return self.categoria.calcular_vendas_categoria(data_inicio, data_fim)
    
    def vendas_por_regiao(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """
        Retorna vendas agregadas por região.
        
        Returns:
            dict: Dados para gráfico de pizza
        """

        return self.regiao.calcular_vendas_por_regiao(data_inicio, data_fim)

    def vendas_por_dia_semana(self, data_inicio: str | None = None, data_fim: str | None = None) -> Dict[str, Any]:
        """
        Retorna vendas agregadas por dia da semana (0=Domingo .. 6=Sábado).
        
        Returns:
            dict: Dados para gráfico de barras horizontal
        """

        return self.sazonalidade.calcular_sazonalidade_dia_semana(data_inicio, data_fim)
    
    def top_produtos(self, data_inicio: str | None = None, data_fim: str | None = None, limite: int = 10) -> Dict[str, Any]:
        """
        Retorna top produtos mais vendidos.
        
        Args:
            limite: Número de produtos a retornar
            
        Returns:
            dict: Dados para gráfico de barras horizontal
        """

        return self.series.calcular_top_produtos(data_inicio, data_fim, limite)
    def vendas_margem_lucro(self, data_inicio: str | None, data_fim: str | None) -> Dict[str, Any]:
        """
        Retorna a margem de lucro entre as Vendas

        Returns:
            dict: Dados para gráfico de barras horizontal
        """

        return self.margem.calcular_margem_lucro(data_inicio, data_fim)

    def vendas_vendedor(self, data_inicio: str | None = None, data_fim: str | None = None, limite: int = 10) -> Dict[str, Any]:
        """
        Retorna vendas agregadas por vendedor.
        
        Args:
            limite: Número de vendedores a retornar
            
        Returns:
            dict: Dados para gráfico de barras horizontal
        """

        return self.vendedor.calcular_vendas_vendedor(data_inicio, data_fim, limite)