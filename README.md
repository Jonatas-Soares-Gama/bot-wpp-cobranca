# Bot Recap

Projeto simples em Python para executar o bot localizado na pasta `app`.

## Estrutura principal

- `app/` - código do bot (arquivo principal `app.py`).
- `.env` - variáveis de ambiente (opcional).
- `requirements.txt` - dependências Python.

## Requisitos

- Python 3.8+ recomendado

## Instalação

1. Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python -m venv .venv
.
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Configure variáveis de ambiente:

- Copie/edite o arquivo `.env` se necessário e defina as variáveis que seu bot precisa.

## Execução

Execute o bot a partir da raiz do diretório `bot`:

```bash
python app/app.py
```

ou (dependendo do `app.py`):

```bash
python -m app.app
```

## Observações

- Este README é uma visão geral mínima. Para detalhes do comportamento do bot, abra `app/app.py`.
- Se houver outro serviço (ex.: `wppconnect-server`) na workspace, este README descreve apenas o subprojeto `bot`.

---

Se quiser, eu posso acrescentar instruções específicas de configuração (variáveis `.env`) ou exemplos de uso.
