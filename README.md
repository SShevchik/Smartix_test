Smartix_test

Запуск
=======

1. Заполнить файл окружения (.env) для backend - Smartix_test/.env:

          DEBUG=False
          SECRET_KEY=секретный ключ приложения
          POSTGRES_USER=логин бд 
          POSTGRES_PASSWORD=пароль бд 
          POSTGRES_DB=название бд
          POSTGRES_HOST=db
          POSTGRES_PORT=5432
          DADATA_KEY=API KEY аккаунта dadata
          DADATA_SECRET=API SECRET аккаунта dadata
          REDIS_HOST=cache
          REDIS_PORT=6379
          NETWORK=127.0.0.1

2. Запустить:

       $ docker-compose up --build

3. Открыть в браузере http://localhost:8000/

# Документация API

### Базовый URL
/api

## Эндпоинты

### Эндпоинты пользователя

### 1. Регистрация
- **URL**: `register/`
- **Метод**: `POST`
- **Описание**: Регистрация пользователя.
- **Параметры запроса**:
  - `username` (string): Имя пользователя.
  - `password` (string): Пароль пользователя.
- **Пример запроса**:
  ```json
  {
    "username": "exampleUser",
    "password": "password123"
  }
  
- **Пример ответа**:
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODk1MjgyOCwiaWF0IjoxNzE4OTA5NjI4LCJqdGkiOiI0OWRmYzI4Y2RlNmQ0ZGNmYmZlN2NkYjNiNTdlY2NkNiIsInVzZXJfaWQiOjF9.DoTPIIC2kH9NEfvjKv4D37z9L7eT6KZjwJGvG97A520",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTI0MDI4LCJpYXQiOjE3MTg5MDk2MjgsImp0aSI6ImQ1MjVhYjY1ZTc5NDQ4MTFiZmE3ZGE5YzBjMzZkNzhlIiwidXNlcl9pZCI6MX0.0D8WokQ5duCyo24krFJdqcSGkM-L4AcZAQo_yZRq7u8"
  }

### 2. Авторизация
- **URL**: `login/`
- **Метод**: `POST`
- **Описание**: Авторизация пользователя.
- **Параметры запроса**:
  - `username` (string): Имя пользователя.
  - `password` (string): Пароль пользователя.
- **Пример запроса**:
  ```json
  {
    "username": "exampleUser",
    "password": "password123"
  }
  
- **Пример ответа**:
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODk1MjgyOCwiaWF0IjoxNzE4OTA5NjI4LCJqdGkiOiI0OWRmYzI4Y2RlNmQ0ZGNmYmZlN2NkYjNiNTdlY2NkNiIsInVzZXJfaWQiOjF9.DoTPIIC2kH9NEfvjKv4D37z9L7eT6KZjwJGvG97A520",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTI0MDI4LCJpYXQiOjE3MTg5MDk2MjgsImp0aSI6ImQ1MjVhYjY1ZTc5NDQ4MTFiZmE3ZGE5YzBjMzZkNzhlIiwidXNlcl9pZCI6MX0.0D8WokQ5duCyo24krFJdqcSGkM-L4AcZAQo_yZRq7u8"
  }

### 2. Обновления токена
- **URL**: `token/refresh/`
- **Метод**: `POST`
- **Описание**: Обновления токена.
- **Параметры запроса**:
  - `refresh` (string): Рефреш токен.
- **Пример запроса**:
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODkzNjY3NCwiaWF0IjoxNzE4ODkzNDc0LCJqdGkiOiI0YTk2YmU1Mjk5NzE0YzI2ODZhOTJmYzRkMjUzNDJjOCIsInVzZXJfaWQiOjEzfQ.Up-Cbzz0GE3EAzbtyZZpR7EpdUPGfwEiDq8wHfdYkL8"
  }
  
- **Пример ответа**:
  ```json
  {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTI0MDI4LCJpYXQiOjE3MTg5MDk2MjgsImp0aSI6ImQ1MjVhYjY1ZTc5NDQ4MTFiZmE3ZGE5YzBjMzZkNzhlIiwidXNlcl9pZCI6MX0.0D8WokQ5duCyo24krFJdqcSGkM-L4AcZAQo_yZRq7u8"
  }

### Эндпоинты модели User

### 1. Получение информации о пользователе
- **URL**: `user/<int:user_id>`
- **Метод**: `GET`
- **Описание**: Получение информации о пользователе по ID.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**: Нет
- **Пример ответа**:
  ```json
  {
    "id": 1,
    "last_login": null,
    "username": "exampleUser",
    "first_name": "",
    "last_name": "",
    "email": "",
    "date_joined": "2024-06-20T10:04:22.546891Z"
  }

### 2. Создание пользователя
- **URL**: `user/`
- **Метод**: `POST`
- **Описание**: Создание нового пользователя. Доступно только пользователям с правами суперпользователя.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**:
  - `username` (string): Имя пользователя.
  - `password` (string): Пароль пользователя.
  - `first_name` (string): Имя пользователя - опциональный.
  - `last_name` (string): Фамилия пользователя - опциональный.
  - `email` (string): Почтовый адрес пользователя - опциональный.
- **Пример запроса**:
  ```json
  {
    "user": {
      "username": "exampleUser",
      "password": "password123"
    }
  }
- **Пример ответа**:
  ```json
  {
    "id": 1,
    "last_login": null,
    "username": "exampleUser",
    "first_name": "",
    "last_name": "",
    "email": "",
    "date_joined": "2024-06-20T10:04:22.546891Z"
  }

### 3. Обновление пользователя
- **URL**: `user/`
- **Метод**: `PUT`
- **Описание**: Обновление информации об аккаунте авторизованного пользователя.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**:
  - `username` (string): Имя пользователя.
  - `password` (string): Пароль пользователя.
  - `first_name` (string): Имя пользователя - опциональный.
  - `last_name` (string): Фамилия пользователя - опциональный.
  - `email` (string): Почтовый адрес пользователя - опциональный.
- **Пример запроса**:
  ```json
  {
    "user": {
      "username": "exampleUser",
      "password": "password123",
      "email": "example@mail.com"
    }
  }
- **Пример ответа**:
  ```json
  {
    "id": 1,
    "last_login": null,
    "username": "exampleUser",
    "first_name": "",
    "last_name": "",
    "email": "example@mail.com",
    "date_joined": "2024-06-20T10:04:22.546891Z"
  }

### 4. Удаление пользователя
- **URL**: `user/`
- **Метод**: `DELETE`
- **Описание**: Удаление аккаунта авторизованного пользователя.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**: Нет
- **Пример ответа**: Нет содержимого, статус код: 204 No Content

### Эндпоинты модели Address

### 1. Получение информации об адресах
- **URL**: `addresses/`
- **Метод**: `GET`
- **Описание**: Получение информации о всех адресах пользователя.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**: Нет
- **Пример ответа**:
  ```json
  [
    {
        "id": 1,
        "source": "спб улица ленина 1",
        "edited": false,
        "postal_code": "197136",
        "country": "Россия",
        "federal_district": "Северо-Западный",
        "region": "Санкт-Петербург",
        "area": null,
        "city": null,
        "city_district": "Петроградский",
        "settlement": null,
        "street_type_full": "улица",
        "street": "Ленина",
        "stead": null,
        "house": "1",
        "block": null,
        "entrance": null,
        "floor": null,
        "flat": null,
        "geo_lat": 59.9583825,
        "geo_lon": 30.3112349,
        "owner": 1
    }
  ]

### 2. Создание адреса
- **URL**: `addresses/`
- **Метод**: `POST`
- **Описание**: Создание нового адреса.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**:
  - `address` (string): Исходная строка поиска адреса.
- **Пример запроса**:
  ```json
  {
    "address": "спб улица ленина 1"
  }
- **Пример ответа**:
  ```json
  {
        "id": 1,
        "source": "спб улица ленина 1",
        "edited": false,
        "postal_code": "197136",
        "country": "Россия",
        "federal_district": "Северо-Западный",
        "region": "Санкт-Петербург",
        "area": null,
        "city": null,
        "city_district": "Петроградский",
        "settlement": null,
        "street_type_full": "улица",
        "street": "Ленина",
        "stead": null,
        "house": "1",
        "block": null,
        "entrance": null,
        "floor": null,
        "flat": null,
        "geo_lat": 59.9583825,
        "geo_lon": 30.3112349,
        "owner": 1
    }

### 3. Обновление адреса
- **URL**: `addresses/<int:address_id>`
- **Метод**: `PUT`
- **Описание**: Обновление информации об адресе пользователя по ID.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**:
  - `postal_code` (string): Индекс - опциональный.
  - `country` (string): Страна - опциональный.
  - `federal_district` (string): Федеральный округ - опциональный.
  - `region` (string): Регион - опциональный.
  - `area` (string): Район в регионе - опциональный.
  - `city` (string): Город - опциональный.
  - `city_district` (string): Район города - опциональный.
  - `settlement` (string): Населенный пункт - опциональный.
  - `street_type_full` (string): Тип улицы - опциональный.
  - `street` (string): Улица - опциональный.
  - `stead` (string): Номер земельного участка - опциональный.
  - `house` (string): Дом - опциональный.
  - `block` (string): Корпус/строение - опциональный.
  - `entrance` (string): Подъезд - опциональный.
  - `floor` (string): Этаж - опциональный.
  - `flat` (string): Квартира - опциональный.
- **Пример запроса**:
  ```json
  {
    "address":{
        "postal_code": "420099"
    }
  }
- **Пример ответа**:
  ```json
  {
        "id": 1,
        "source": "спб улица ленина 1",
        "edited": false,
        "postal_code": "420099",
        "country": "Россия",
        "federal_district": "Северо-Западный",
        "region": "Санкт-Петербург",
        "area": null,
        "city": null,
        "city_district": "Петроградский",
        "settlement": null,
        "street_type_full": "улица",
        "street": "Ленина",
        "stead": null,
        "house": "1",
        "block": null,
        "entrance": null,
        "floor": null,
        "flat": null,
        "geo_lat": 59.9583825,
        "geo_lon": 30.3112349,
        "owner": 1
    }

### 4. Удаление адреса
- **URL**: `addresses/<int:address_id>/`
- **Метод**: `DELETE`
- **Описание**: Удаление адреса пользователя по ID.
- **Заголовок авторизации**: Требуется
  - `Authorizarion: Bearer <access_token>`
- **Параметры запроса**: Нет
- **Пример ответа**: Нет содержимого, статус код: 204 No Content