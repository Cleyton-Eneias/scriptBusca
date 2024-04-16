import PyPDF2
import os

pesqdiretorio = input("Diretório dos arquivos: ")
busca_nome = input("Matricula ou Nome: ")

ano_inicio = int(input("inicio: "))
ano_fim = int(input("fim: "))

def buscar_e_salvar_pagina_com_nome(nome_arquivo_pdf, nome_a_buscar, diretorio_saida):
    with open(nome_arquivo_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for pagina_num in range(len(pdf_reader.pages)):
            pagina = pdf_reader.pages[pagina_num]
            texto = pagina.extract_text()
            
            if nome_a_buscar in texto:
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(pagina)
                
                nome_arquivo_saida = os.path.join(diretorio_saida, os.path.splitext(os.path.basename(nome_arquivo_pdf))[0] + " com " + nome_a_buscar + ".pdf")
                with open(nome_arquivo_saida, 'wb') as pdf_saida:
                    pdf_writer.write(pdf_saida)
                
                print(f"Página com o nome '{nome_a_buscar}' encontrada no arquivo '{nome_arquivo_pdf}' e salva em '{nome_arquivo_saida}'.")
                return
            
        print(f"O nome '{nome_a_buscar}' não foi encontrado no arquivo '{nome_arquivo_pdf}'.")

diretorio_pdfs= pesqdiretorio
nome_a_buscar = busca_nome
diretorio_saida = r"C:\Users\Admin\Desktop\PUSH FICHA FINACEIRAS\saida"


for ano in range(ano_inicio, ano_fim+1):
    nome_arquivo_pdf = os.path.join(diretorio_pdfs, f"{ano}.pdf")
    buscar_e_salvar_pagina_com_nome(nome_arquivo_pdf, nome_a_buscar, diretorio_saida)
