"""Aplicação Flask que expõe os validadores via formulário web.

Para rodar localmente:
    flask --app src.app run
"""

from flask import Flask, jsonify, render_template, request

from src.validators import validar_cpf, validar_email, validar_telefone


def criar_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/validar")
    def validar():
        dados = request.get_json(silent=True) or request.form
        cpf = dados.get("cpf", "")
        email = dados.get("email", "")
        telefone = dados.get("telefone", "")
        return jsonify(
            cpf_valido=validar_cpf(cpf),
            email_valido=validar_email(email),
            telefone_valido=validar_telefone(telefone),
        )

    return app


app = criar_app()


if __name__ == "__main__":
    app.run()
