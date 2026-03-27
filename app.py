from modelos.args_cli import ArgumentosCLI
from modelos.paths import Path_List

param = ArgumentosCLI()

print(param)

diretorios = Path_List.listar_caminhos(param.entrada)

# for i in diretorios:
#     print(i)
#     print(i.name)
#     print(i.suffix)

Path_List.organizar(diretorios, param.saida)


# entrada = '/home/cairo/Área de Trabalho/desafios/copiar/entrada/contrato1.pdf'
# saida = '/home/cairo/Área de Trabalho/desafios/copiar/saida/contrato1.pdf'

# Path_List.organizar(entrada, saida)