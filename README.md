# Products-storage-service

<br>

## Contents:
- [Description](#description)
- [Technology](#technology)
- [Customization and startup](#customization-and-startup)
- [Testing the service](#testing-the-service)
<br>


## Description

The service of products storage, realizing CRUD-operations with additional functionality “Reduction of the number of products in the warehouse”.


<details><summary>List</summary>

**Programming languages, libraries and modules:**

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)

**Framework, extensions and libraries:**

[![Django](https://img.shields.io/badge/Django-v5.1.2-blue?logo=Django)](https://www.djangoproject.com/)

**Databases**

[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)

[⬆️Contents](#contents)

</details>


## Customization and startup

1. Cloning a repository.
    ```bash
   git clone https://github.com/Ilya-kutylev/Products-storage-service.git
   cd Products-storage-service
   ```
2. Installing and updating package managers (pip, pipenv).
    ```bash
   pip install --upgrade pip \
   && pip install pipenv
    ```
3. Creating a virtual environment and installing dependencies.
    ```bash
   pipenv install
   pipenv shell
    ```
4. Apply migrations to create the necessary tables in the database.
    ```bash
    python manage.py migrate
    ```
5. Before launching the service, it is necessary to create a superuser for authorization in the admin panel.
    ```bash
    python manage.py createsuperuser
    ```
   - To start the service, run the command:
   ```bash
    python manage.py runserver
   ```
   

## Testing the service

It is recommended to use the postman program to test API requests.

## 📚 API эндпоинты

| Метод  | URL                                  | Описание                                |
|--------|--------------------------------------|-----------------------------------------|
| GET    | `/api/v1/products/`                  | Получить список всех товаров            |
| GET    | `/api/v1/products/{id}/`             | Получить данные о товаре по ID          |
| POST   | `/api/v1/products/`                  | Создать новый товар                     |
| PATCH  | `/api/v1/products/{id}/`             | Частично обновить данные товара по ID   |
| PUT    | `/api/v1/products/{id}/`             | Полностью обновить данные товара по ID  |
| DELETE | `/api/v1/products/{id}/`             | Удалить товар по ID                     |
| PATCH  | `/api/v1/products/{id}/reduce-stock/`| Уменьшить количество товара на складе   |
