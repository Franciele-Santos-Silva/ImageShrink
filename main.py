from PIL import Image
import os

pasta = 'images'

lista_arquivos = os.listdir(pasta)

for nome_arquivo in lista_arquivos:
    imagem = Image.open(os.path.join(pasta, nome_arquivo))

    imagem = imagem.convert('P', palette=Image.ADAPTIVE)

    novo_nome = os.path.join(pasta, f'reduzido_ {nome_arquivo}')
    imagem.save(novo_nome, optimize= True)

