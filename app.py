from flask import Flask, render_template, request, jsonify
from encrypt import encrypt, decrypt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/processar", methods=["POST"])
def processar():
    dados = request.json
    chave_principal = dados.get("chave_principal")
    bloco_dados = dados.get("bloco_dados")
    operacao = dados.get("operacao")
    if operacao == "decrip":
        bloco_final = decrypt(chave_principal, bloco_dados)
    else:
        bloco_final = encrypt(chave_principal, bloco_dados)
    # Processa os dados utilizando suas funções
    resposta = {
        "bloco_final": bloco_final
    }
    return jsonify(resposta)

if __name__ == "__main__":
    app.run(debug=True)
