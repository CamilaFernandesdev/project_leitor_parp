import pandas as pd
from pathlib import Path


def leitor_ree(caminho: Path) -> tuple:
    """_summary_.

    Args:
        caminho (Path): caminho do arquivo REE.DAT

    Returns:
        1. df_ree(pd.Dataframe)
        2. nomes_ree(tuple): nomes dos reservatórios equivalente de energia.
    """
    #Dados do REE
    df_ree = pd.read_fwf(caminho, skiprows=3, skipfooter=1, header=None)
    # Hard Code, futura substituição  do nome da coluna
    cab = ['NUM', 'NOME REES', 'SUBM']
    df_ree.columns = cab
    
    # Nome dos REEs
    # E como chave do dict parp
    nomes_ree = tuple(df_ree['NOME REES'])
    
    return df_ree, nomes_ree
    


if __name__ == '__main__':
    #Arquivo original
    arquivo_ree = Path('arquivos\REE (1).DAT')
    ree, nomes_ree = leitor_ree(arquivo_ree)
    
