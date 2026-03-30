from pathlib import Path

class Path_List:
    @classmethod
    def listar_caminhos(self, entrada: Path) -> list:
        p = Path(entrada)
        arq_caminhos = list()
        for x in p.rglob('*/.'):
            if not x.is_dir():
                arq_caminhos.append(x)

        if len(arq_caminhos) == 0:
            print('Diretório informado não existe ou está vazio')
            exit()
            
        print('Entrada de arquivos com caminho:')
        for index,i in enumerate(arq_caminhos, start=1):
            print(f'{index} -> {i}')
        print()

        return arq_caminhos
    

