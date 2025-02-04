# Como executar o código
## Configurando o ambiente
- Usando ambiente virtual:
    - Criar o ambiente virtual, no Windows(PowerShell, CMD) e no Linux(Bash, Zsh): ```python -m venv venv```
    - Ativar o ambiente virtual:
        - Windows: ```.\venv\Script\activate```
        - Linux: ```./venv/bin/activate```
    - Instalar as dependências: ```pip install -r requirements.txt```
## Executar os scripts
Para executar os scripts definidos a seguir, os comandos destacados devem ser executados no terminal aberto dentro da pasta do projeto. E em relação ao script principal, os arquivos .xlsx devem estar dentro de uma pasta "files" na raiz do projeto.
- Scripts do Banco de Dados:
    - Criar as tabelas no banco: ```python controller.py db_create_tables```
    - Excluir as tabelas no banco: ```python controller.py db_drop_tables```
- Script Principal:
    - Processar os arquivos .xlsx e inserir no banco: ```python controller.py process```