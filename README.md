# Django Cars

## 📘 Sobre

Sistema desenvolvido em Django para gerenciamento de informações sobre carros.

## 💻️ Tecnologias

- Python
- Django
- SQLite

## ✅ Funcionalidade

- [x] Cadastro de usuários
- [x] Listagem, criação, atualização e deleção de carros
- [x] Busca de carros por modelo ou marca

## ⚙️ Instalação e Execução

1. Clone o repositório e navegue para a pasta do projeto:

```bash
git clone https://github.com/elainefs/django-cars.git

cd django-cars
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv # Para Windows use: python -m venv .venv
source .venv/bin/activate  # Para Windows use: .venv\Scripts\activate
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

4. Execute as migrações no banco de dados:

```bash
python3 manage.py migrate
```

5. Crie um super usuário:

```bash
python3 manage.py createsuperuser
```

6. Execute a aplicação:

```bash
python3 manage.py runserver
```

A aplicação estará disponível em `http://localhost:8000`.

O gerenciamento também pode ser feito através da interface do Django Admin em: `http://localhost:8000/admin/`.

## 📄 Licença

Este projeto está sobre a licença MIT. Veja o arquivo [LICENSE](https://github.com/elainefs/django-cars/blob/main/LICENSE) para mais informações.

---

Made with ❤️ by [Elaine Ferreira](https://github.com/elainefs)