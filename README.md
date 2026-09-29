# Проект домашней работы Django_22

1. Клонируйте репозиторий:
```
https://github.com/oMakom/CoursePaperOOP_DB.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
poetry install
```
Проект подготовлен на Django.

В приложении `catalog` реализованы домашняя страница `home.html`
и страница с контактной информацией `contacts.html`

При отправке данных формы контактов выходит сообщение о успешной отправке.

В приложении созданы три модели `Category` `Product` `Contact`
### Category
- наименование -> name
- описание -> description
### Product
- наименование -> name
- описание -> description
- изображение -> image
- категория -> category - связана с Category
- цена за покупку -> price
- дата создания -> created_at
- дата последнего изменения -> updated_at
### Contact
- имя -> name
- почта -> email
- сообщение -> message

Сформированы миграции для всех моделей и фикстура для заполения продуктов и категорий.
Реализована команда add_products для очистки базы данных и заполнения ее из фикстуры.