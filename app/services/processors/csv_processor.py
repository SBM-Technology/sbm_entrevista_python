from typing import List
import pandas as pd
from flask import current_app
from werkzeug.datastructures import FileStorage
from app import db
from app.models import Venda

class CsvProcessor:

    COLUNAS_OBRIGATORIAS_VENDAS = [
        'data', 'produto', 'categoria', 'quantidade',
        'preco_unitario', 'regiao', 'vendedor'
    ]
    COLUNAS_OBRIGATORIAS_CUSTOS = ['produto', 'categoria', 'custo_unitario']

    """Processa arquivos CSV."""
    
    def processar_vendas_custos(self, file: FileStorage, tipo: str) -> int:
        """Processa arquivo CSV de vendas ou custos"""
        try:
            # Lê CSV
            df = pd.read_csv(file)
            
            # Valida colunas obrigatórias
            if tipo == 'vendas':
                colunas_obrigatorias = self.COLUNAS_OBRIGATORIAS_VENDAS
            elif tipo == 'custos':
                colunas_obrigatorias = self.COLUNAS_OBRIGATORIAS_CUSTOS
            else:
                raise ValueError(f"Tipo inválido: {tipo}")

            self._validar_colunas(df, colunas_obrigatorias)
            
            # Processa cada linha
            registros_processados = self._processa_salva_registros(df)
            return registros_processados
            
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao processar {tipo}: {e}")

    def _processa_salva_registros(self, df: pd.DataFrame) -> int:
        """Processa e salva os registros no banco de dados"""
        # Processa cada linha
        registros_processados = 0
        for _, row in df.iterrows():
            try:
                # Calcula valor total
                valor_total = row['quantidade'] * row['preco_unitario']
                
                venda = Venda(
                    data=pd.to_datetime(row['data']).date(),
                    produto=str(row['produto']),
                    categoria=str(row['categoria']),
                    quantidade=int(row['quantidade']),
                    preco_unitario=float(row['preco_unitario']),
                    valor_total=valor_total,
                    regiao=str(row['regiao']),
                    vendedor=str(row['vendedor'])
                )
                
                db.session.add(venda)
                registros_processados += 1
                
            except Exception as e:
                current_app.logger.warning(f"Erro ao processar linha: {e}")
                continue
        
        db.session.commit()
        return registros_processados

    def _validar_colunas(self, df: pd.DataFrame, colunas_obrigatorias: List[str]) -> None:
        """Valida se DataFrame possui colunas obrigatórias."""
        colunas_faltantes = set(colunas_obrigatorias) - set(df.columns)
        if colunas_faltantes:
            raise ValueError(
                f"Colunas obrigatórias faltando: {', '.join(colunas_faltantes)}"
            )