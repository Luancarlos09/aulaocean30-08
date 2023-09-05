from flask import Flask
from flask import render_template
app = Flask("Meu App")
posts = [{
        "titulo" : "Minha primeira postagem",
        "texto" : "test"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts #mock das postagens
    return render_template ('exibir_entradas.html', entradas=entradas)
@app.route('/layout')
def layout():
    return render_template ('layout.html')