### Executar o projeto
``python3 app.py --entrada ./entrada --saida ./saida --limpar``

--entrada: Informar caminho do diretório que será manipulado

--saida: Informar diretório onde será salvo os arquivos manipulados

--limpar: (opcional) Apaga os arquivos do diretório de saida antes de gerar

### Saida
Os arquivos organizados são copiados para o diretório de saida e organizados pela extensão em sua respectiva pasta.

Arquivos sem extensão ou não identificados são agrupados na pasta "outros".

Os arquivos organizados mantêm o nome original, porém com prefixo numerico no inicio para ordenamento e tratamento de possiveis duplicidades de subdiretorios da entrada.

É gerado um relatório na raiz, contendo um resumo de arquivos processados, contador de tipo de arquivos e mapeamento de origem X destino dos arquivos.


