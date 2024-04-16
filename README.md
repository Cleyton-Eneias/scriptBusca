# Documentação do Script de Busca em Arquivos PDF
Este script Python foi desenvolvido para buscar um nome específico em arquivos PDF dentro de um diretório especificado e salvar as páginas contendo esse nome em novos arquivos PDF.

Requisitos
Python 3.x 
Biblioteca PyPDF2
Instalação das Dependências


Para instalar a biblioteca PyPDF2, execute o seguinte comando no terminal:
```
pip install PyPDF2
```
Como Usar:
Clone ou faça o download deste repositório para sua máquina local.

Execute o script pdf_name_search.py em um ambiente Python.

O script solicitará as seguintes informações:

Diretório onde os arquivos PDF estão localizados.
Nome ou matrícula a ser buscado nos arquivos PDF.
Ano de início e ano de fim para a busca nos arquivos PDF.
Após fornecer as informações solicitadas, o script realizará a busca nos arquivos PDF no intervalo de anos especificado e salvará as páginas contendo o nome buscado em novos arquivos PDF em um diretório de saída.

Exemplo de Uso:
```
import PyPDF2
import os

# Função para buscar e salvar páginas com o nome especificado
def buscar_e_salvar_pagina_com_nome(nome_arquivo_pdf, nome_a_buscar, diretorio_saida):
    ...

# Diretório onde os arquivos PDF estão e nome a buscar

diretorio_pdfs = input("Diretório dos arquivos: ")
nome_a_buscar = input("Matricula ou Nome: ")
ano_inicio = int(input("Início: "))
ano_fim = int(input("Fim: "))
diretorio_saida = r"C:\Users\Admin\Desktop\PUSH FICHA FINACEIRAS\saida"

# Loop para buscar nos arquivos PDF de cada ano no intervalo especificado
for ano in range(ano_inicio, ano_fim+1):
    nome_arquivo_pdf = os.path.join(diretorio_pdfs, f"{ano}.pdf")
    buscar_e_salvar_pagina_com_nome(nome_arquivo_pdf, nome_a_buscar, diretorio_saida)
```
Notas
Certifique-se de que os arquivos PDF estão localizados no diretório especificado e que você tem permissão de leitura e escrita nesse diretório.
Os arquivos PDF de entrada devem estar formatados de forma que o texto seja extraível corretamente.
Este script foi testado em sistemas Windows. A compatibilidade com outros sistemas operacionais pode variar.
O script não faz distinção entre maiúsculas e minúsculas ao buscar o nome nos arquivos PDF.
