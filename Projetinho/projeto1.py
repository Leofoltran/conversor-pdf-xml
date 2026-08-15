import pdfplumber

def extrair_texto(caminho_pdf):
    texto_por_pagina = []
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            texto_por_pagina.append(texto)
    return texto_por_pagina

# Teste rápido
paginas = extrair_texto("Currículo_Leonardo.pdf")
print(f"O PDF tem {len(paginas)} página(s)")
print(paginas[0][:500])  # mostra os primeiros 500 caracteres da primeira página


def separar_paragrafos(texto_pagina):
    paragrafos = texto_pagina.split("\n\n")
    
    if len(paragrafos) <= 1:
        paragrafos = texto_pagina.split("\n")
    
    paragrafos = [p.strip() for p in paragrafos if p.strip()]
    return paragrafos 

paginas = extrair_texto("Currículo_Leonardo.pdf")
paragrafos = separar_paragrafos(paginas[0])
print(f"Encontrei {len(paragrafos)} parágrafo(s) na primeira página")
for p in paragrafos[:3]:
    print("---")
    print(p)