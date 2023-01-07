#  API для определения шаблона формы

![](https://github.com/katecapri/images-for-readme/blob/main/011.png) 
  ![](https://github.com/katecapri/images-for-readme/blob/main/012.png)


##  Описание ##

В базе данных MongoDB хранятся шаблоны форм. Поля в формах могут быть 4 типов:
1. Дата в формате DD.MM.YYYY или YYYY-MM-DD.
2. Телефон в формате +7 ХХХ ХХХ ХХ ХХ.
3. E-mail.
4. Текст.

POST-запросом по адресу http://127.0.0.1/get_form/ передается произвольный список полей с данными.
Ответом выдается название шаблона из имеющейся коллекции, который содержит указанные поля и соответствует типам пришедшей информации. Если такого шаблона в коллекции нет, возвращаются полученные поля и соответствующий им тип данных из 4 имеющихся. 
GET-запросом по адресу http://127.0.0.1/get_form/ выводятся все имеющиеся шаблоны в БД.

##  Используемые технологии ##

- Python 3.10.2
- Docker
- fastapi==0.87.0
- pymongo==4.3.3
- requests==2.28.1
- uvicorn==0.20.0


##  Инструкция по запуску ##

1. Инициализировать новый репозиторий в папке:

> git init

2. Загрузить репозиторий с проектом:

> git pull https://github.com/katecapri/choose-template-api.git

3. Запустить контейнеры:

> docker-compose up

4. Просмотр запущенных контейнеров:

> docker ps

5. Через консоль контейнера choose_template 

> docker exec -it CONTAINER_ID bash

или с помощью Docker Desktop заполнить БД:

> python3 fill_collection.py


##  Результат ##

- По адресу <http://127.0.0.1/get_form/> без наполнения БД открывается пустая страница.

![](https://github.com/katecapri/images-for-readme/blob/main/013.png)

- После добавления шаблонных форм в коллекцию по адресу <http://127.0.0.1/get_form/> выдается список имеющихся форм.

![](https://github.com/katecapri/images-for-readme/blob/main/014.png)

- На скришоте ниже выводится результат работы API, когда информация по 5 запросам не была найдена (до наполнения БД шаблонными формами) и когда для 3 запросов шаблон существует, а для 2 подходящего шаблона нет.

![](https://github.com/katecapri/images-for-readme/blob/main/010.png)

- Пример обращения через Postman.

![](https://github.com/katecapri/images-for-readme/blob/main/015.png)
