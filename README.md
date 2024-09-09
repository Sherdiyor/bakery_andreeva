# Bakery Andreeva

Welcome to Bakery Andreeva, a web application that showcases our delicious cakes and provides an easy way to order them online.

## Features

- **Cake Catalog:** Browse our extensive catalog of cakes, including descriptions, prices, and images.
- **New Arrivals:** Stay up-to-date with our latest cake creations and promotions.
- **Order Form:** Easily place an order online with our convenient and user-friendly form.

## API Documentation

Our API is built using OpenAPI 3.0.3 and provides a comprehensive set of endpoints for interacting with our cake catalog and ordering system. You can find the API documentation at /api/schema/.

## Security

Our API uses token-based authentication with a required prefix "Token". You can obtain a token by making a POST request to /api-token-auth/ with your username and password.

## Endpoints

### Cake Catalog:
- GET /api/catalog/: Retrieve a list of all cakes.
- GET /api/catalog/{id}/: Retrieve a specific cake by ID.
- POST /api/catalog/: Create a new cake.
- PUT /api/catalog/{id}/: Update a cake.
- PATCH /api/catalog/{id}/: Partially update a cake.
- DELETE /api/catalog/{id}/: Delete a cake.

### Order Form:
- GET /api/form/: Retrieve a list of all orders.
- GET /api/form/{id}/: Retrieve a specific order by ID.
- POST /api/form/: Create a new order.
- PUT /api/form/{id}/: Update an order.
- PATCH /api/form/{id}/: Partially update an order.
- DELETE /api/form/{id}/: Delete an order.

### New Arrivals:
- GET /api/hots/: Retrieve a list of new arrivals.
- GET /api/hots/{id}/: Retrieve a specific new arrival by ID.
- POST /api/hots/: Create a new arrival.
- PUT /api/hots/{id}/: Update a new arrival.
- PATCH /api/hots/{id}/: Partially update a new arrival.
- DELETE /api/hots/{id}/: Delete a new arrival.

## Technologies

- **Backend:** Built using Python and Django.
- **Frontend:** Built using HTML, CSS, and JavaScript.
- **Database:** Powered by PostgreSQL.

## Contributing

If you'd like to contribute to Bakery Andreeva, please fork this repository and submit a pull request. We appreciate any help in making our application better!

## License

Bakery Andreeva is licensed under the MIT License.

# Также на русском языке

# Пекарня Андреева

Добро пожаловать в Пекарню Андрееву — веб-приложение, которое демонстрирует наши вкусные торты и предоставляет удобный способ их заказа онлайн.

## Особенности

- **Каталог тортов:** Просмотрите наш обширный каталог тортов, включая описания, цены и изображения.
- **Новинки:** Будьте в курсе наших последних творений и акций.
- **Форма заказа:** Легко оформите заказ онлайн с помощью нашей удобной формы.

## Документация API

Наш API построен с использованием OpenAPI 3.0.3 и предоставляет полный набор конечных точек для взаимодействия с нашим каталогом тортов и системой заказа. Вы можете найти документацию API по адресу /api/schema/.

## Безопасность

Наш API использует аутентификацию на основе токенов с обязательным префиксом "Token". Вы можете получить токен, сделав POST-запрос на /api-token-auth/ с вашим именем пользователя и паролем.

## Конечные точки

### Каталог тортов:
- GET /api/catalog/: Получить список всех тортов.
- GET /api/catalog/{id}/: Получить конкретный торт по ID.
- POST /api/catalog/: Создать новый торт.
- PUT /api/catalog/{id}/: Обновить торт.
- PATCH /api/catalog/{id}/: Частично обновить торт.
- DELETE /api/catalog/{id}/: Удалить торт.

### Форма заказа:
- GET /api/form/: Получить список всех заказов.
- GET /api/form/{id}/: Получить конкретный заказ по ID.
- POST /api/form/: Создать новый заказ.
- PUT /api/form/{id}/: Обновить заказ.
- PATCH /api/form/{id}/: Частично обновить заказ.
- DELETE /api/form/{id}/: Удалить заказ.

### Новинки:
- GET /api/hots/: Получить список новинок.
- GET /api/hots/{id}/: Получить конкретную новинку по ID.
- POST /api/hots/: Создать новую новинку.
- PUT /api/hots/{id}/: Обновить новинку.
- PATCH /api/hots/{id}/: Частично обновить новинку.
- DELETE /api/hots/{id}/: Удалить новинку.

## Технологии

- **Бэкенд:** Построен на Python и Django.
- **Фронтенд:** Построен на HTML, CSS и JavaScript.
- **База данных:** Используется PostgreSQL.

## Участие

Если вы хотите внести свой вклад в Пекарню Андрееву, пожалуйста, сделайте форк этого репозитория и отправьте запрос на слияние. Мы ценим любую помощь в улучшении нашего приложения!

## Лицензия

Пекарня Андреева лицензирована под MIT License.