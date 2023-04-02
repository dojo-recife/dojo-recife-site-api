# DOJO Recife API

API do site do Dojo Recife

## Quer contribuir com o desenvolvimento?

1. Clone o repositório.
```console
git clone git@github.com:dojo-recife/dojo-recife-site-api.git dojo_recife_api
cd dojo_recife_api
```
2. Crie um virtualenv com Python 3.8
```console
python -m venv venv
```
3. Ative o virtualenv.
```console
source venv/bin/activate
```
4. Instale as dependências.
```console
pip install -r requirements.txt
```
5. Configure a instância com o .env
```console
cp .env-example .env
```
6. Execute os testes.
```console
pytest
```

### Extra:
 - Gere uma SECRET_KEY executando o comando:
    ```console
   python contrib/secret_gen.py
   ```