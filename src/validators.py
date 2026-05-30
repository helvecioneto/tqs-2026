"""Validadores de CPF e e-mail.

Lógica de negócio pura, sem dependência de framework web.
Pensada para ser exercitada via TDD na disciplina PC010027 (UFOPA).
"""

import re

_REGEX_EMAIL = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def _calcular_digito_verificador(digitos: str, peso_inicial: int) -> int:
    pesos = range(peso_inicial, 1, -1)
    soma = sum(int(d) * peso for d, peso in zip(digitos, pesos, strict=True))
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto


def validar_cpf(cpf: str | None) -> bool:
    if not isinstance(cpf, str):
        return False

    apenas_digitos = re.sub(r"[.\-\s]", "", cpf)

    if len(apenas_digitos) != 11 or not apenas_digitos.isdigit():
        return False

    if len(set(apenas_digitos)) == 1:
        return False

    primeiro = _calcular_digito_verificador(apenas_digitos[:9], peso_inicial=10)
    segundo = _calcular_digito_verificador(apenas_digitos[:10], peso_inicial=11)

    return apenas_digitos[9] == str(primeiro) and apenas_digitos[10] == str(segundo)


def validar_email(email: str | None) -> bool:
    if not isinstance(email, str) or not email:
        return False
    return _REGEX_EMAIL.match(email) is not None


# Implementação de funções para CNPJ


def _calcular_dv_cnpj(digitos: str, pesos: list[int]) -> int:
    soma = sum(int(d) * p for d, p in zip(digitos, pesos, strict=True))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def validar_cnpj(cnpj: str | None) -> bool:
    if not isinstance(cnpj, str):
        return False
    apenas_digitos = re.sub(r"[.\-/\s]", "", cnpj.strip())
    if len(apenas_digitos) != 14 or not apenas_digitos.isdigit():
        return False
    if len(set(apenas_digitos)) == 1:
        return False
    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro = _calcular_dv_cnpj(apenas_digitos[:12], pesos_primeiro)
    segundo = _calcular_dv_cnpj(apenas_digitos[:13], pesos_segundo)
    return apenas_digitos[12] == str(primeiro) and apenas_digitos[13] == str(segundo)


def validar_telefone(telefone: str | None) -> bool:
    if not isinstance(telefone, str):
        return False
    apenas_digitos = re.sub(r"[()\-\s]", "", telefone.strip())
    if len(apenas_digitos) != 11 or not apenas_digitos.isdigit():
        return False
    ddd = int(apenas_digitos[:2])
    if not (11 <= ddd <= 99):
        return False
    return apenas_digitos[2] == "9"

