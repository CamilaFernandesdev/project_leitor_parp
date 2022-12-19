from pathlib import Path
import re



def extract_parts_text_file(caminho: str,
                            regex_ini: str,
                            regex_fim: str,
                            skip_rowns=0,
                            skip_footer=0):
    """_summary_

    Args:
        caminho (str): arquivo de texto
        regex_ini (str): _description_
        regex_fim (str): _description_
        skip_rowns (int): _description_
        skip_footer (int): _description_

    Returns: file_stringIO (object): formato compatível com pandas 
            
    """
    arquivo = Path(caminho)
    
    with open(arquivo, 'r') as f:
        text = f.readlines()
        
    pattern = re.compile(regex_ini)
    pattern2 = re.compile(regex_fim)



    posicao_ini = None
    posicao_fim = None
    for i, line in enumerate(text):
        match1 = pattern.search(line)
        if match1:
            posicao_ini = i
            break
            

    for i, line in enumerate(text):
        match2 = pattern2.search(line)
        if match2:    
            posicao_fim = i
            break
            
            
    trecho = text[posicao_ini + skip_rowns: posicao_fim - skip_footer]

    trecho_text = ''.join(trecho)
    #file_stringIO = StringIO(trecho_text)
    
    return trecho_text



if __name__ == '__main__':
    
    sudeste = r'.*SERIE  DE ENERGIAS DO REE.*SUDESTE.*(CONFIGURACAO No.    1).*'
    end_intervalo = r'.*MEDIA AMOSTRAL DAS ENERGIAS.*'
