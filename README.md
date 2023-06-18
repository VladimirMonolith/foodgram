# Cервис Foodgram, "Продуктовый помощник"    

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Описание

Онлайн-сервис Foodgram и API для него.Имеется реализация CI/CD проекта.На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список "Избранное", а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Доступный функционал

- Аутентификация реализована с помощью стандартного модуля DRF - Authtoken.
- У неаутентифицированных пользователей доступ к API только на уровне чтения.
- Создание объектов разрешено только аутентифицированным пользователям.На прочий фунционал наложено ограничение в виде административных ролей и авторства.
- Управление пользователями.
- Возможность получения подробной информации о себе и ее редактирование.
- Возможность подписаться на других пользователей и отписаться от них.
- Получение списка всех тегов и ингредиентов.
- Получение списка всех рецептов, их добавление.Получение, обновление и удаление конкретного рецепта.
- Возможность добавить рецепт в избранное.
- Возможность добавить рецепт в список покупок.
- Возможность скачать список покупок в PDF формате.
- Фильтрация по полям.

#### Документация к API доступна по адресу <http://localhost/api/docs/> после локального запуска проекта

#### Технологи

- Python 3.7
- Django 3.2.15
- Django Rest Framework 3.12.4
- Authtoken
- Docker
- Docker-compose
- PostgreSQL
- Gunicorn
- Nginx
- GitHub Actions
- Выделенный сервер Linux Ubuntu 22.04 с публичным IP

#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
   git clone <название репозитория>
```

```bash
   cd <название репозитория> 
```

Cоздать и активировать виртуальное окружение:

Команда для установки виртуального окружения на Mac или Linux:

```bash
   python3 -m venv env
   source env/bin/activate
```

Команда для Windows:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

- Перейти в директорию infra:

```bash
   cd infra
```

- Создать файл .env по образцу:

```bash
   cp .env.example .env
```

- Выполнить команду для доступа к документации:

```bash
   docker-compose up 
```

Установить зависимости из файла requirements.txt:

```bash
   cd ..
   cd backend
   pip install -r requirements.txt
```

```bash
   python manage.py migrate
```

Заполнить базу тестовыми данными об ингредиентах:

```bash
   python manage.py load_ingredients_data
```

Создать суперпользователя, если необходимо:

```bash
python manage.py createsuperuser
```

- Запустить локальный сервер:

```bash
   python manage.py runserver
```

#### Установка на удалённом сервере

- Выполнить вход на удаленный сервер
- Установить docker:

```bash
   sudo apt install docker.io
   ```

- Установить docker-compose:

``` bash
    sudo apt install docker-compose     
```

или воспользоваться официальной [инструкцией](https://docs.docker.com/compose/install/)

- Находясь локально в директории infra/, скопировать файлы docker-compose.yml и nginx.conf на удаленный сервер:

```bash
scp docker-compose.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
```

- Для правильной работы workflow необходимо добавить в Secrets данного репозитория на GitHub переменные окружения:

```bash
Переменные PostgreSQL, ключ проекта Django и их значения по-умолчанию можно взять из файла .env.example, затем установить свои.

DOCKER_USERNAME=<имя пользователя DockerHub>
DOCKER_PASSWORD=<пароль от DockerHub>

USER=<username для подключения к удаленному серверу>
HOST=<ip сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш приватный SSH-ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<id вашего Телеграм-аккаунта>
TELEGRAM_TOKEN=<токен вашего бота>
```

#### Workflow проекта

- **запускается при выполнении команды git push**
- **tests:** проверка кода на соответствие PEP8.
- **build_and_push_to_docker_hub:** сборка и размещение образа проекта на DockerHub.
- **deploy:** автоматический деплой на боевой сервер и запуск проекта.
- **send_massage:** отправка уведомления пользователю в Телеграм.

#### После успешного результата работы workflow зайдите на боевой сервер

- Примените миграции:

```bash
   sudo docker-compose exec backend python manage.py migrate
```

- Подгружаем статику:

```bash
   sudo docker-compose exec backend python manage.py collectstatic --no-input
```

- Заполните базу тестовыми данными об ингредиентах:

```bash
   sudo docker-compose exec backend python manage.py load_ingredients_data
```

- Создайте суперпользователя:

```bash
   sudo docker-compose exec backend python manage.py createsuperuser
```

#### Примеры некоторых запросов API

Регистрация пользователя:

```bash
   POST /api/v1/users/
```

Получение данных своей учетной записи:

```bash
   GET /api/v1/users/me/ 
```

Добавление подписки:

```bash
   POST /api/v1/users/id/subscribe/
```

Обновление рецепта:
  
```bash
   PATCH /api/v1/recipes/id/
```

Удаление рецепта из избранного:

```bash
   DELETE /api/v1/recipes/id/favorite/
```

Получение списка ингредиентов:

```bash
   GET /api/v1/ingredients/
```

Скачать список покупок:

```bash
   GET /api/v1/recipes/download_shopping_cart/
```

Проект доступен по адресу: <http://foodgram-diplom.myddns.me/>

Доступ в админку:

```bash
   email - ad@min.com
   пароль - sh7811vu
```

Пользователь:

```bash
   email - dima@dima.com
   пароль - am2471383
```

#### Полный список запросов API находятся в документации

#### Автор

Гут Владимир - [https://github.com/VladimirMonolith](http://github.com/VladimirMonolith)
