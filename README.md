# AskPupkin

## Страницы / роуты

| URL | Описание |
|-----|----------|
| `/` | Список новых вопросов |
| `/hot/` | Список популярных вопросов |
| `/tag/<name>/` | Вопросы по тегу |
| `/question/<id>/` | Страница одного вопроса |
| `/ask/` | Форма создания вопроса |
| `/login/` | Форма входа |
| `/signup/` | Форма регистрации |
| `/profile/` | Редактирование профиля |

## Запуск локально

```bash
python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Открыть: http://127.0.0.1:8000/

## Запуск через Docker Compose

```bash
sudo docker-compose up --build
```

Открыть: http://localhost:8000/
