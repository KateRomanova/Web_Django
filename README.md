Сайт интернет магазина

Содержит каталог с товарами, их описанием, изображением, ценой.
Есть возможность получать подробную информацию о продуктах и редактировать ее, а также добавлять и удалять продукты 
в зависимости от прав доступа пользователя.

Раздел блога позволяет размещать статьи, редактировать и удалять их. Установлен счетчик просмотров.

Для корректной работы приложения необходимо установить следующие зависимости:
[tool.poetry.dependencies]
python = "^3.12"
psycopg2-binary = "^2.9.9"
black = "^24.4.2"
pillow = "^10.3.0"
ipython = "^8.25.0"
articles = "^0.1.0"
article = "^0.1.1"
django = "4.2.2"
nullable = "^0.2.0"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
