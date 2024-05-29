# MyFitness

### Развертывание

- **(_Опционально_)** Создать виртуальное окружение и выполнять все команды ниже в нем
- Установить зависимости командой `pip install -r requirements.txt`
- Создать и применить миграции командами `python manage.py makemigrations` и `python manage.py migrate`
- **(_Опционально_)** Создать администратора `python manage.py auto_superuser`
- Доступ к панели администрирования Django http://127.0.0.1:8000/admin

### Запуск

- Запуск производится командой `python manage.py runserver`
- Запуск celery `celery -A myfitness worker -l info --pool=solo`
- Запуск redis `cd redis` `start redis-server`


### Авторизация
- Авторизация происходит с помощью токенов. Когда пользователь создается, то получает уникальный токен. В дальнейшем он
должен указываться в header запроса следующим образом `Authorization: Token <token_key>`