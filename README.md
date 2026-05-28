# TQS 2026 — Projeto-exemplo de Teste e Qualidade de Software

> Material didático da disciplina **Teste e Qualidade de Software (PC010027)** — graduação, Universidade Federal do Oeste do Pará (UFOPA).
> Prof. **Helvecio Bezerra Leal Neto** · 2026

Este repositório é um **livro prático em capítulos**. Construímos juntos uma pequena aplicação web (um validador de CPF e e-mail) e usamos cada etapa para demonstrar um conceito da disciplina: testes automatizados, TDD, qualidade de código, CI/CD, deploy automatizado e workflow de Pull Requests.

A ideia é que você **leia e execute cada capítulo em ordem**, terminando com um projeto completo que você reproduziu do zero.

🌐 **Demo público**: `https://<seu-usuario>.github.io/tqs-2026/`

---

## 📖 Sumário do livro

| # | Capítulo | O que você aprende |
|---|---|---|
| 1 | [Visão geral](capitulos/01-visao-geral.md) | Sobre a aplicação, decisões arquiteturais, stack |
| 2 | [Preparando o ambiente](capitulos/02-preparando-ambiente.md) | Pré-requisitos (Git, Python, IDE), criar repo, venv |
| 3 | [Rodando a aplicação](capitulos/03-rodando-aplicacao.md) | Subir o Flask local, testar manualmente, entender o fluxo |
| 4 | [Testes automatizados](capitulos/04-testes-automatizados.md) | Unitários vs integração, pytest, cobertura, `parametrize` |
| 5 | [TDD na prática](capitulos/05-tdd-na-pratica.md) | Ciclo Red→Green→Refactor, walkthrough completo |
| 6 | [Qualidade de código](capitulos/06-qualidade-de-codigo.md) | ruff (lint+format), bandit (segurança), cobertura como portão |
| 7 | [CI com GitHub Actions](capitulos/07-ci-github-actions.md) | Pipeline `ci.yml` linha-a-linha, lendo logs de falha |
| 8 | [Deploy automatizado](capitulos/08-deploy-automatizado.md) | GitHub Pages, workflow `deploy.yml`, configuração inicial |
| 9 | [Pull Requests](capitulos/09-pull-requests.md) | Fluxo de PR, branch protection, code review, CODEOWNERS |
| 10 | [Atividade prática](capitulos/10-atividade-pratica.md) | 5 tarefas hands-on (CNPJ via TDD, quebrar o CI, etc.) |
| 11 | [Recursos & Licença](capitulos/11-recursos-e-licenca.md) | Documentação, bibliografia, para ir além |

> 💡 Cada capítulo tem navegação **anterior ↔ próximo**, então você pode lê-los de ponta a ponta como um livro.

---

## ⚡ Quick start (GitHub Codespaces)

Esta disciplina usa **GitHub Codespaces** como ambiente único — zero instalação, tudo no navegador. O [capítulo 2](capitulos/02-preparando-ambiente.md) cobre o setup em detalhes.

1. **Fork** este repositório (ou crie o seu seguindo o capítulo 2).
2. No seu repo, clique em **Code** → aba **Codespaces** → **Create codespace on main**.
3. Aguarde ~1 minuto. O VS Code abre no navegador com tudo instalado (Python 3.11, dependências, extensões).
4. No terminal do Codespace:

```bash
pytest                              # 6 testes, 82% cobertura
flask --app src.app run             # porta 5000 será exposta automaticamente
```

> Trabalhar localmente (com Python instalado) ou pelo github.dev (navegador sem terminal) também funciona, mas não vamos cobrir — padronizamos em Codespaces.

### Verificações que o CI roda (antes de cada commit)

```bash
ruff check . && ruff format --check .
bandit -r src/
pytest --cov=src --cov-fail-under=80
```

---

## 🗂️ Estrutura do repositório

```
tqs-2026/
├── .devcontainer/
│   └── devcontainer.json           # config GitHub Codespaces
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                  # lint + testes + cobertura
│   │   └── deploy.yml              # deploy GitHub Pages
│   ├── ISSUE_TEMPLATE/             # templates de issue
│   ├── pull_request_template.md    # checklist obrigatório de PRs
│   └── CODEOWNERS                  # quem revisa o quê
├── capitulos/                      # 📖 ESTE LIVRO (11 capítulos)
├── src/
│   ├── validators.py               # ⭐ VERSÃO PRINCIPAL da lógica
│   ├── app.py                      # rotas Flask
│   └── templates/index.html        # formulário (Flask)
├── tests/
│   ├── test_validators.py          # 4 testes unitários
│   └── test_app.py                 # 2 testes de integração
├── docs/                           # publicado no GitHub Pages
│   ├── index.html
│   ├── validators.js               # espelho JS de validators.py
│   └── style.css
├── pyproject.toml                  # config ruff + pytest + coverage
├── requirements.txt                # Flask
├── requirements-dev.txt            # pytest, ruff, bandit
├── LICENSE                         # MIT
└── README.md                       # você está aqui
```

---

## 🎯 Status atual

| Métrica | Valor |
|---|---|
| Testes | **6 passando** (4 unitários + 2 integração) |
| Cobertura | **82%** (piso do CI: 80%) |
| Lint | ✅ ruff sem warnings |
| Segurança | ✅ bandit sem issues |

> Por que só 6 testes? A suíte é proposital­mente enxuta — o objetivo é que você **leia, entenda e expanda**. A [atividade prática](capitulos/10-atividade-pratica.md) pede para você adicionar testes de casos de borda (todos dígitos iguais, tamanho errado, etc.) usando TDD.

---

## 📜 Licença

[MIT](LICENSE) — use, modifique e distribua livremente, inclusive em sala de aula.

---

**Comece a leitura** → [Capítulo 1 — Visão geral ➡](capitulos/01-visao-geral.md)

TESTE
