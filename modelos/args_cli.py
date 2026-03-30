import argparse

class ArgumentosCLI:
    '''Verifica os argumentos passados via CLI...'''

    def __init__(self):
        self.parametros_cli = argparse.ArgumentParser(description='Manipulador de arquivos e diretórios')
        self.parametros_cli.add_argument('--entrada', type=str, help='Diretório que será manipulado')
        self.parametros_cli.add_argument('--saida', type=str, help='Diretório que será salvo os arquivos manipulados')
        self.parametros_cli.add_argument('--limpar', action='store_true', help='Apagar arquivos do diretório de saida antes de gerar')
        self.args = self.parametros_cli.parse_args()
        self.entrada = self._get_entrada()
        self.saida = self._get_saida()

    def __str__(self):
        return (
            f'Caminho entrada: {self.entrada}\n'
            f'Caminho saida: {self.saida}\n'
            f'Limpar saida: {self.args.limpar}\n'
            )

    
    def _get_entrada(self) -> str:
        entrada = self.args.entrada
        if entrada == None:
            entrada = input(str('Digite o caminho da pasta que gostaria de organizar: '))
        return entrada
    
    def _get_saida(self) -> str:
        if self.args.saida == None:
            return './saida/' 
        return self.args.saida 
    



