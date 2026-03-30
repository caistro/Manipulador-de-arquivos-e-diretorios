from pathlib import Path
import shutil
import os
from collections import Counter

class Organizer:
    mapa = dict()
    resumo_tipo = list()

    @classmethod
    def organizar(cls, entrada: list[Path], saida: Path, limpar: bool=False) -> None:
        if limpar is True:
            shutil.rmtree(saida)
            
        print('Saida de arquivos com caminho:')
        for index, arq in enumerate(entrada, start=1):
            extensao = arq.suffix[1:]
            if extensao == '':
                extensao = 'outros'
            out = f'{saida}{extensao}/'
            cls.resumo_tipo.append(extensao)
            os.makedirs(out, exist_ok=True)
            quantidade = Counter(cls.resumo_tipo).get(extensao)
            print(f'{index} -> {out}{quantidade}_{arq.name}')
            shutil.copy2(arq, f'{out}{quantidade}_{arq.name}')
            cls.mapa.update({str(arq):f'{out}{quantidade}_{arq.name}'})
        
    @classmethod
    def salva_txt(cls,saida:Path) -> None:
        with open(f'{saida}relatório.txt', 'w', encoding='utf-8') as relatorio:
            relatorio.write(f'Total de arquivos processados: {len(cls.resumo_tipo)}')
            relatorio.write('\n\n')
            relatorio.write('Resumo por tipo:\n')
            for k,v in Counter(cls.resumo_tipo).items():
                relatorio.write(f'{k}: {v}\n')
            relatorio.write('\n')
            relatorio.write('Mapeamento:\n')
            for index, (k,v) in enumerate(cls.mapa.items(), start=1):
                relatorio.write(f'{index}: {k} -> {v}\n')

