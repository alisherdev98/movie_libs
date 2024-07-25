# Movie Library API

Этот проект представляет собой API для управления библиотекой фильмов, разработанный на Django с использованием Django REST Framework. Он включает функции для добавления, получения, обновления и удаления фильмов, а также предоставляет документацию API с помощью Swagger и ReDoc.

## Содержание

1. [Установка](#установка)
2. [Настройка](#настройка)
3. [Запуск](#запуск)
4. [Документация API](#документация-api)
5. [Лицензия](#лицензия)

## Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/alisherdev98/movie_libs
cd movie-libs
```

### 2. Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

## Настройка
### 1. Создайте файлы миграции
```bash
python manage.py createmigrations
```
### 2. Выполните миграции
bash
python manage.py migrate

### 3. Создайте суперпользователя
```bash
python manage.py createsuperuser
```

### 4. Необходимо загрузить данные по жанрам
Принимает 2 позиционных аргумента:
- file_path - путь до файла с данными по жанрам;
- file_type - тип файла с данными по жанрам(json, csv);

```bash
python manage.py load_genres /file/to/path/data.json json
```

## Запуск
Запустите сервер Django:

```bash
python manage.py runserver
```

## Документация API
Документация API доступна по следующим адресам:

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/

## Лицензия
Этот проект лицензирован под BSD License.