# wishlist_project

Список желаний на Django (проект для студентов Цифровой кафедры, 2024–2025): регистрация и вход, добавление, редактирование и удаление своих желаний.

**Стек:** Python 3, Django 5.1, SQLite.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Приложение откроется на http://127.0.0.1:8000/.

## Настройки через переменные окружения

| Переменная | По умолчанию | Описание |
|---|---|---|
| `DJANGO_SECRET_KEY` | небезопасный dev-ключ | Обязательно задайте свой в продакшене |
| `DJANGO_DEBUG` | `1` | `0` для продакшена |

## Лицензия

[MIT](LICENSE)
