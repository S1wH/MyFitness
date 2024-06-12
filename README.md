# MyFitness

### Развертывание

- **(_Опционально_)** Создать виртуальное окружение и выполнять все команды ниже в нем
- Установить зависимости командой `pip install -r requirements.txt`
- Создать и применить миграции командами `python manage.py makemigrations` и `python manage.py migrate`
- **(_Опционально_)** Создать администратора `python manage.py auto_superuser`
- Доступ к панели администрирования Django http://127.0.0.1:8000/admin

### Запуск

#### Windows

   1) Запсук Redis:
      - `cd redis`
      - `start redis-server`
   2) Запуск Celery:
      - `celery -A myfitness worker -l info --pool=solo`
   3) Запуск Веб-Сервера
      - `python manage.py runserver`

#### Linux

   1) Запсук Redis:
      - `sudo apt-get install redis`
      - `redis-server`
   2) Запуск Celery:
      - `celery -A myfitness worker -l info --pool=solo`
   3) Запуск Веб-Сервера
      - `python manage.py runserver`


### Авторизация
- Авторизация происходит с помощью токенов. Когда пользователь создается, то получает уникальный токен. В дальнейшем он
должен указываться в header запроса следующим образом `Authorization: Token <token_key>`

### Чаты
- Доступ к чатам происходит по средствам websockets
- Для присоедниения к чату нужно отправить запрос на `ws://127.0.0.1:8000/ws/chat/<conversation_id>`, где <conversation_id> - id чата
- Для корректного запроса требуется указывать токен отправителя сообщения в заголовках, как и при обычном запросе, т.е. `Authorization: Token <token_key>`
- При отправке сообщения будет возвращена контактная информация о нем