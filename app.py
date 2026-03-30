from modelos.args_cli import ArgumentosCLI
from modelos.diretorio import Path_List
from modelos.organizador import Organizer

param = ArgumentosCLI()
print(param)

try:
    diretorios = Path_List.listar_caminhos(param.entrada)
    Organizer.organizar(diretorios, param.saida, param.args.limpar)
    Organizer.salva_txt(param.saida)
except PermissionError:
    print('Sem permissão para acessar o diretório informado')