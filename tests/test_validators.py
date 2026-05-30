"""Testes unitários dos validadores de CPF e e-mail.

Mantemos a suíte propositalmente pequena: 1 caso válido + 1 caso inválido
para cada validador. O suficiente para o aluno acompanhar o ciclo TDD
sem se afogar em código de teste.

Os capítulos 5 (TDD) e 10 (atividade prática) sugerem novos testes
para cobrir casos de borda — adicione-os à medida que evoluir o projeto.
"""

from src.validators import validar_cpf, validar_email, validar_cnpj, validar_telefone


def test_aceita_cpf_valido():
    assert validar_cpf("111.444.777-35") is True


def test_rejeita_cpf_com_digito_verificador_errado():
    assert validar_cpf("111.444.777-30") is False


def test_aceita_email_valido():
    assert validar_email("aluno@ufopa.edu.br") is True


def test_rejeita_email_sem_arroba():
    assert validar_email("semarroba.com") is False

def test_aceita_telefone_valido_com_mascara():
    assert validar_telefone("(11) 91234-5678") is True


def test_aceita_telefone_valido_sem_mascara():
    assert validar_telefone("11912345678") is True


def test_rejeita_telefone_sem_nono_digito():
    assert validar_telefone("(11) 81234-5678") is False


def test_rejeita_telefone_com_ddd_invalido():
    assert validar_telefone("(10) 91234-5678") is False


def test_rejeita_telefone_com_tamanho_errado():
    assert validar_telefone("1191234567") is False
