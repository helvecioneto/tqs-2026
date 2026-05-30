"""Testes de integração das rotas Flask.

Mostram como exercitar a aplicação sem subir servidor de fato,
usando o test client do próprio Flask. Mantemos só dois testes
(um por rota) para foco didático.
"""

import pytest

from src.app import criar_app


@pytest.fixture
def client():
    app = criar_app()
    return app.test_client()


def test_index_retorna_formulario(client):
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert "Teste e Qualidade de Software" in resposta.get_data(as_text=True)


def test_validar_retorna_resultados_corretos(client):
    resposta = client.post(
        "/validar",
        json={
            "cpf": "111.444.777-35",
            "email": "aluno@ufopa.edu.br",
            "telefone": "(11) 91234-5678",
        },
    )
    assert resposta.get_json() == {
        "cpf_valido": True,
        "email_valido": True,
        "telefone_valido": True,
    }
