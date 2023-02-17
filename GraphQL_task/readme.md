# Тестовое задание на стажировку в Росатом
## Задание повышенной сложности (GraphQL API)
[![Generic badge](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/)


### Установка
___
> pip install -r requirements.txt


### Описание
___
Файл `main.py` содержит код по синхронизации GraphQL API, FastApi.

В коде представлена условная база данных (БД). С помощью GraphQL запросов из БД можно получить нужную информацию. 

### Старт программы
___
- Для старта работы программы запустите файл `task_2_code_review.py`.
- Перейдите по адресу: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
- Введите в поле слева следующий код взамен шаблона для получения :
```
{
  users{
    name,
    age
  },
  rockets{
    name,
    link
  }
}
```
