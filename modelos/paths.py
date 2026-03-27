from pathlib import Path
import shutil
import os

class Path_List:
    @classmethod
    def listar_caminhos(self, entrada: Path) -> list:
        p = Path(entrada)
        arq_caminhos = list()
        for x in p.rglob('*/.'):
            if not x.is_dir():
                arq_caminhos.append(x)
        return arq_caminhos
    
    @classmethod
    def organizar(self, entrada: list[Path], saida: Path) -> None:            
        for arq in entrada:
            extensao = arq.suffix[1:]
            if extensao == '':
                extensao = 'outros'
            out = f'{saida}{extensao}/'
            print(out)
            os.makedirs(out, exist_ok=True)
            quantidade = len([f for f in Path(out).iterdir()])+1
            print(quantidade)
            shutil.copy2(arq, f'{out}{quantidade}_{arq.name}')



