## Redes II


## Projeto de Arquitetura em 3 Camadas com Docker

Esse projeto foi feito pra disciplina de **Redes de Computadores II**, com o objetivo de montar uma aplicação web simples usando arquitetura de 3 camadas. Para facilitar a execução e a organização, usamos **Docker** e **Docker Compose** pra gerenciar os contêineres — uma solução prática e eficiente, mesmo que às vezes pareça que cada ferramenta adiciona mais passos do que deveria.

### Estrutura da Solução

A aplicação segue a arquitetura em **3 camadas**, que separa responsabilidades e deixa tudo mais modular, o que é um ponto positivo claro.

**Camada de Apresentação:** É a interface com o usuário, acessada pelo navegador em `http://localhost:5000`. Funciona bem e cumpre exatamente o que se espera: mostrar a aplicação de forma simples e direta.

**Camada Lógica (Servidor Web):** Desenvolvida em **Python** com **Flask**, rodando em um contêiner Docker. Essa camada processa as requisições e fala com o banco de dados. É eficiente e a integração com Flask é direta, embora seja fácil perceber que pequenos erros de configuração podem travar tudo se não forem corrigidos.

**Camada de Dados (Banco de Dados):** Usamos **PostgreSQL** em outro contêiner separado. A persistência de dados é garantida e a separação das camadas faz sentido.

### Tecnologias Usadas

* **Docker & Docker Compose:** Excelente para criar, gerenciar e orquestrar os contêineres. Pouco criticável, pois simplifica bastante a execução.
* **Python 3.9:** Linguagem clara e adequada para essa aplicação.
* **Flask:** Micro-framework que facilita muito a criação do servidor web.
* **PostgreSQL 14 (14-alpine):** Robusto e leve.
* **Psycopg2-binary:** Faz a comunicação entre Python e PostgreSQL funcionar sem complicações.
* **Git & GitHub:** Essenciais para versionamento e controle de alterações.

### Como Rodar

Precisa ter **Docker** e **Docker Compose** instalados.

1. **Pré-requisito:** Docker Desktop instalado.
2. **Arquivos:** Não é obrigatório clonar o repositório, basta ter `docker-compose.yml` e `Dockerfile`.
3. **Rodar:** Abra o terminal na pasta e execute:

```bash
docker-compose up --build
```

O `--build` cria a imagem da aplicação, garantindo que tudo esteja configurado corretamente. Um passo a mais, mas necessário.

4. **Acessar:** Abra o navegador em:

```
http://127.0.0.1:5000/
```

### Resultado Esperado

Se tudo estiver correto, verá a mensagem:

``
Que deu certo e a conexão com a base de dados foi bem sucedida 




