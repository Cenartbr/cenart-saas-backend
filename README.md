# CENART SaaS - Backend (Flask API)

Este é o backend da aplicação SaaS para a CENART, desenvolvido em Flask (Python).

## Visão Geral

A API fornece endpoints para gerenciar os módulos Financeiro, de Projetos e Comercial da empresa CENART.

## Estrutura do Projeto

-   `src/`: Contém o código fonte da aplicação.
    -   `main.py`: Ponto de entrada principal da aplicação Flask, configuração e inicialização.
    -   `models/`: Define os modelos de dados (SQLAlchemy) para interação com o banco de dados MySQL.
    -   `routes/`: Contém os blueprints do Flask para organizar as rotas de cada módulo (financeiro, projetos, comercial).
    -   `static/`: (Opcional) Para arquivos estáticos, se o backend servir alguma interface diretamente.
-   `venv/`: Ambiente virtual Python com as dependências do projeto.
-   `requirements.txt`: Lista de todas as dependências Python do projeto.

## Módulos da API (Blueprints)

-   **/api/financeiro**: Endpoints para Contas a Pagar, Contas a Receber, Fluxo de Caixa, etc.
-   **/api/projetos**: Endpoints para Projetos, Tarefas, Custos de Projeto, etc.
-   **/api/comercial**: Endpoints para Clientes, Orçamentos, Oportunidades, etc.

## Banco de Dados

Utiliza MySQL, com modelos definidos em `src/models/`. As tabelas são criadas automaticamente na primeira execução (para desenvolvimento) e os dados iniciais (como papéis e status) são semeados.

## Como Executar Localmente (para Desenvolvimento)

1.  Certifique-se de ter Python 3.11+ e pip instalados.
2.  Clone o repositório (se aplicável).
3.  Crie e ative o ambiente virtual:
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5.  Configure as variáveis de ambiente para o banco de dados MySQL (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME). Por padrão, ele tentará se conectar a `root:password@localhost:3306/mydb`.
6.  Execute a aplicação:
    ```bash
    python src/main.py
    ```
    A API estará disponível em `http://localhost:5001`.

## Endpoints Principais (Exemplos)

-   `GET /health`: Verifica a saúde da aplicação.
-   `GET /`: Mensagem de boas-vindas da API.
-   `GET /api/financeiro/contas_pagar`: Lista contas a pagar (exemplo).
-   `GET /api/projetos/`: Lista projetos (exemplo).
-   `GET /api/comercial/clientes`: Lista clientes (exemplo).

(Esta documentação é um resumo inicial. Uma documentação mais detalhada dos endpoints, incluindo payloads de requisição/resposta, seria gerada usando ferramentas como Swagger/OpenAPI para um projeto completo.)

