# API for article comments

## description
This is a test task for an interview

## formulation of the problem

### Реализовать REST API для системы комментариев блога.
##### Функциональные требования:
У системы должны быть методы API, которые обеспечивают
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
- Добавление комментария к статье.
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
- Получение всех комментариев к статье вплоть до 3 уровня вложенности.
- Получение всех вложенных комментариев для комментария 3 уровня.
- По ответу API комментариев можно воссоздать древовидную структуру.

##### Нефункциональные требования:
- Использование Django ORM.
- Следование принципам REST.
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
- Решение в виде репозитория на Github, Gitlab или Bitbucket.
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv.
- Использование свежих версий python и Django.

##### Будет плюсом:
- Использование PostgreSQL.
- docker-compose для запуска api и базы данных.
- Swagger либо иная документация к апи.

## installation
```console
pip3 install git+https://github.com/Flash-kir/testAPI
pip3 install recuirenments.txt
python manage.py runserver
```
## models
#### Article
|field|type|
|-----|----|
|id|BigAutoField(primary_key=True)|
|title|CharField(max_length=64, null=True, blank=True)|
|text|TextField()|

#### Comment
|field|type|
|-----|----|
|id|BigAutoField(primary_key=True)|
|artcle|ForeignKey(Article, on_delete=models.PROTECT)|
|parent|IntegerField()|
|author|CharField(max_length=32, null=True, blank=True)|
|level|IntegerField()|
|text|TextField()|
## api

### add object Article
##### request
|type|url|json params|
|----|---|-----------|
|POST |/api/articles/|```{"title": "str64 param","text": "text param"}```|

##### return
```json
{
  "status": "200",
  "article id": "int"
}
```

### add object Comment
##### request
|type|url|json params|
|----|---|-----------|
|POST |/api/comments/|{"author": "str32","text": "text","article_id": "int","parent_id": "int"}|

##### return
```json
{
  "status": "200",
  "comment id": "int"
}
```

### get comments for Article with depth
##### request
|type|url|url params|json params|
|----|---|-----|-----------|
|POST |/api/article/{article_id}/comments/|"article_id" type "int"|{"max_level": "int - the depth of comment tree, set 0 to get all child comments"}|

##### return
```json
{
  "level": "int - depth level of comment(for article level is 0)",
  "number": "int - number of child comments to use in cycle(use keys from '0' to 'number - 1')",
  "child":
  {
    "0":
    {
      "level": "int",
      "number": "int",
      "author": "str32 - comment author name",
      "text": "text - comment text",
      "id": "int - comment id",
      "child": {}
    }
  }
}
```
##### JSON response example
```json
{
  "level": 0,
  "number": 4,
  "child": {
    "0": {
      "level": 1,
      "number": 0,
      "author": "anon",
      "text": "text of comment",
      "id": 1,
      "child": {}
    },
    "1": {
      "level": 1,
      "number": 1,
      "author": "name2",
      "text": "text of comment 2",
      "id": 2,
      "child": {
        "level": 2,
        "number": 0,
        "author": "anon3",
        "text": "text of comment 3",
        "id": 3,
        "child": {}
        }     
      }
  }
}
```
### get comments for Comment with depth
##### request
|type|url|url params|json params|
|----|---|-----|-----------|
|POST |/api/comment/{comment_id}/comments/|"comment_id" type "int"|{"max_level": "int - the depth of comment tree, set 0 to get all child comments"}|

##### return
```json
{
  "level": "int - depth level of comment(for article level is 0)",
  "number": "int - number of child comments to use in cycle(use keys from '0' to 'number - 1')",
  "child":
  {
    "0":
    {
      "level": "int",
      "number": "int",
      "author": "str32 - comment author name",
      "text": "text - comment text",
      "id": "int - comment id",
      "child": {}
    }
  }
}
```

##### JSON response example
```json
{
  "level": 3,
  "number": 1,
  "child": {
    "0": {
      "level": 4,
      "number": 1,
      "child": {
        "0": {
          "level": 5,
          "number": 2,
          "child": {
            "0": {
              "level": 6,
              "number": 0,
              "child": {},
              "author": "dasgfg",
              "text": "text lvl6",
              "id": 11
            },
            "1": {
              "level": 6,
              "number": 0,
              "child": {},
              "author": "dasgfg",
              "text": "text lvl6 second",
              "id": 12
            }
          },
          "author": "dasgfg",
          "text": "text lvl5",
          "id": 10
        }
      },
      "author": "qwrty",
      "text": "text lvl4",
      "id": 9
    }
  }
}
