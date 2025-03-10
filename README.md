# 🥋 API REST para Academia de Jiu-Jitsu

Uma API RESTful desenvolvida com Python e Django, utilizando Django Ninja, para gerenciar alunos e aulas em uma academia de Jiu-Jitsu.
Este projeto foi desenvolvido durante a imersão "4 Days 4 Projects - Edição 2" da Pythonando.

## 🚀 Funcionalidades

- Criar aluno (`POST /`)
- Listar alunos (`GET /students/`)
- Consultar progresso do aluno (`GET /progress_student/`)
- Registrar aula realizada (`POST /aula_realizada/`)
- Atualizar aluno pelo ID (`PUT /alunos/{student_id}/`)

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Django
- Django Ninja (para criação da API)
- SQLite (banco de dados)

## 🔧 Instalação e Execução

1. Clone este repositório:
  - Utilizando **HTTPS**:
      ```bash
      git clone https://github.com/nascimentocode/Rest-API_JiuJitsu.git
      ```
  - Ou utilizando **SSH**:
    ```bash
    git clone git@github.com:nascimentocode/Rest-API_JiuJitsu.git
    ```

2. Acesse a pasta do projeto:
  ```bash
  cd Rest-API_JiuJitsu
  ```

3. Crie um ambiente virtual e ative-o:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate  # Windows
  ```

4. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

5. Rode as migrações do banco de dados:
  ```bash
  python manage.py migrate
  ```

6. Inicie o servidor:
  ```bash
  python manage.py runserver
  ```

7. Acesse a documentação interativa da API:
  ```bash
  http://127.0.0.1:8000/api/docs
  ```

## 📌 Exemplo de Requisição

Criar um aluno (`POST /`)
```json
{
  "name": "Carlos Silva",
  "email": "carlos@email.com",
  "belt": "B",
  "birthdate": "2000-05-17"
}
```

Listar alunos (`GET /students/`)
```json
[
  {
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "belt": "B",
    "birthdate": "2000-05-17"
  }
]
```

Consultar progresso do aluno (`GET /progress_student/`)
```json
{
  "email": "carlos@email.com"
}
```

- Resposta esperada:
  ```json
  {
    "email": "carlos@email.com",
    "name": "Carlos Silva",
    "belt": "B",
    "total_class": 12,
    "classes_required_for_next_belt": 18
  }
  ```

Registrar aula (`POST /aula_realizada/`)
```json
{
  "qtd": 1,
  "student_email": "carlos@email.com"
}
```

Atualizar um aluno (`PUT /alunos/{student_id}`)
```json
{
  "name": "Carlos Silva Antares",
  "email": "carlos.silva@email.com",
  "belt": "B",
  "birthdate": "2000-05-17"
}
```

## 📝 **Licença**

Este projeto foi desenvolvido durante a imersão **"4 Days 4 Projects - Edição 2" da Pythonando** e está disponível apenas para fins de estudo.
