#  API ��� ����������� ������� �����

![](https://github.com/katecapri/images-for-readme/blob/main/011.png) 
  ![](https://github.com/katecapri/images-for-readme/blob/main/012.png)


##  �������� ##

� ���� ������ MongoDB �������� ������� ����. ���� � ������ ����� ���� 4 �����:
1. ���� � ������� DD.MM.YYYY ��� YYYY-MM-DD.
2. ������� � ������� +7 ��� ��� �� ��.
3. E-mail.
4. �����.

POST-�������� �� ������ http://127.0.0.1/get_form/ ���������� ������������ ������ ����� � �������.
������� �������� �������� ������� �� ��������� ���������, ������� �������� ��������� ���� � ������������� ����� ��������� ����������. ���� ������ ������� � ��������� ���, ������������ ���������� ���� � ��������������� �� ��� ������ �� 4 ���������. 
GET-�������� �� ������ http://127.0.0.1/get_form/ ��������� ��� ��������� ������� � ��.

##  ������������ ���������� ##

- Python 3.10.2
- Docker
- fastapi==0.87.0
- pymongo==4.3.3
- requests==2.28.1
- uvicorn==0.20.0


##  ���������� �� ������� ##

1. ���������������� ����� ����������� � �����:

> git init

2. ��������� ����������� � ��������:

> git pull https://github.com/katecapri/choose-template-api.git

3. ��������� ����������:

> docker-compose up

4. �������� ���������� �����������:

> docker ps

5. ����� ������� ���������� choose_template 

> docker exec -it CONTAINER_ID bash

��� � ������� Docker Desktop ��������� ��:

> python3 fill_collection.py


##  ��������� ##

- �� ������ <http://127.0.0.1/get_form/> ��� ���������� �� ����������� ������ ��������.

![](https://github.com/katecapri/images-for-readme/blob/main/013.png)

- ����� ���������� ��������� ���� � ��������� �� ������ <http://127.0.0.1/get_form/> �������� ������ ��������� ����.

![](https://github.com/katecapri/images-for-readme/blob/main/014.png)

- �� �������� ���� ��������� ��������� ������ API, ����� ���������� �� 5 �������� �� ���� ������� (�� ���������� �� ���������� �������) � ����� ��� 3 �������� ������ ����������, � ��� 2 ����������� ������� ���.

![](https://github.com/katecapri/images-for-readme/blob/main/010.png)

- ������ ��������� ����� Postman.

![](https://github.com/katecapri/images-for-readme/blob/main/015.png)
