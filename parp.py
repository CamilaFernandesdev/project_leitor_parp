
"""
MODELO ESTOCASTICO DE GERACAO DE ENERGIAS SINTETICAS - PAR(p).
"""

from pathlib import Path
from io import StringIO
import pandas as pd

from extract_parts_text_file import extract_parts_text_file
from leitor_ree import leitor_ree



parp_dict = dict()

#Caminhos
arquivo_ree = Path('arquivos/REE (1).DAT')
arquivo_parp = r'arquivos/parp2021.dat'

#---------------------------------------
sudeste = r'.*SERIE  DE ENERGIAS DO REE.*SUDESTE.*(CONFIGURACAO No.    1).*'
end_intervalo = r'.*MEDIA AMOSTRAL DAS ENERGIAS.*'
#---------------------------------------


ree, nomes_ree = leitor_ree(arquivo_ree)
parp = extract_parts_text_file(arquivo_parp,
                               regex_ini=sudeste,
                               regex_fim=end_intervalo,
                               skip_rowns=3,
                               skip_footer=2)

parp_stringio = StringIO(parp)

# Dataframe dos trechos selecionados do parp
df = pd.read_fwf(parp_stringio)
df.set_index(df.columns[0], inplace=True)
df.index.name = 'ANOS'


# Trabalhando com o dicionário
"""
{'SUDESTE': None,
 'MADEIRA': None,
 'TPIRES': None,
 'ITAIPU': None,
 'PARANA': None,
 'PRNPANEMA': None,
 'SUL': None,
 'IGUACU': None,
 'NORDESTE': None,
 'NORTE': None,
 'BMONTE': None,
 'MAN-AP': None}
"""
parp_dict = parp_dict.fromkeys(nomes_ree)


for keys, values in parp_dict.items():
    start_intervalo = r'.*SERIE  DE ENERGIAS DO REE.*{keys}.*(CONFIGURACAO No.    1).*'
    end_intervalo = r'.*MEDIA AMOSTRAL DAS ENERGIAS.*'
    
    
    
    
    
    print(start_intervalo)
