# Preenchedor de Cadastro Automatizado

Este projeto utiliza a biblioteca BotCity para preencher um formulário de cadastro com dados de um arquivo Excel. O script automatiza o processo de inserção de informações em um site de contabilidade, facilitando a tarefa de cadastro em massa.

## Requisitos

- Python 3.x
- `botcity-web` (Biblioteca para automação de navegadores)
- `webdriver-manager` (Gerenciador de drivers para navegadores)
- `pandas` (Biblioteca para manipulação de dados)
- `openpyxl` (Necessário para ler arquivos Excel)

Você pode instalar as dependências necessárias com o seguinte comando:

```bash
pip install botcity-web webdriver-manager pandas openpyxl
```

## Funcionamento
- `Inicialização`: O script inicia uma instância do navegador Firefox usando o WebBot da BotCity.
- `Acesso ao Site`: Acessa o site de contabilidade especificado e maximiza a janela do navegador.
- `Login`: Preenche os campos de email e senha e realiza o login.
- `Leitura do Arquivo Excel`: Lê os dados do arquivo Excel fornecido.
- `Preenchimento do Formulário`: Preenche o formulário no site com as informações extraídas do arquivo Excel.
- `Finalização`: Para o navegador após o preenchimento do formulário.

##Uso:
Para utilizar o script, siga as etapas abaixo:

Prepare o Arquivo Excel: Crie um arquivo Excel (empresas.xlsx) com as seguintes colunas:

-Nome da Empresa
-Email
-Telefone
-Endereço
-CNPJ
-Área de Atuação
-Quantidade de Funcionários
-Data de Fundação

#Execute o Script: Execute o script:
```bash
pyhon bot.py
```
