from fpdf import FPDF

# Criar o objeto PDF
pdf = FPDF()
pdf.add_page()

# Definir a fonte e o tamanho
pdf.set_font('Arial', '', 12)

# Pegar os nomes dos arquivos
arquivo = input('Digite o nome do arquivo com a extensão ->>> ')
nome = input('Agora dê um novo nome para o arquivo ->>> ')

# Abrir o arquivo de texto e adicionar o conteúdo ao PDF
with open(arquivo, 'r') as a:
    for linha in a:
        pdf.cell(0, 10, txt=linha, ln=True)  # ln=True quebra a linha após adicionar a célula

# Salvar o PDF com o novo nome
pdf.output(f'{nome}.pdf')

print(f'PDF {nome}.pdf criado com sucesso!')
