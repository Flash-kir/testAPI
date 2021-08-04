# testAPI
test API for article comments

project api

requests:

- add Article
POST
url: http://127.0.0.1:8000/api/articles/
JSON body params:
"title" - str param, is Article title
"text" - TextField param, is Article text

return:
JSON
{
  "status": "200", - status
  "article id": 16 - ID of new article
}


- add Comment
POST
url: http://127.0.0.1:8000/api/comments/
JSON body params:
"author" - str param, is Comment author name
"text" - TextField param, is Comment text
"article_id" - int param, the ID of article
"parent_id" - int param, mean ID of parent comment,
              if comment is not answer for another set 0

return:
JSON
{
  "status": "200", - status
  "comment id": 12 - ID of new comment
}

- get comments for Article with depth
POST
url: http://127.0.0.1:8000/api/article/1/comments/
where 1 in URL is ID of Article
JSON body params:
"max_level" - int param, mean depth of comments tree

return:
JSON {
  "level": 0,   - level 0 mean that comments belong to article
  "number": 4,  - number of child comments for use in cycle
  "child": {
    "0": { - number of comment for use in cycle
      "level": 1,
      "number": 0, - number of child comments for use in cycle
      "author": "anon", - author name
      "text": "text of comment", - text
      "id": 1,     - ID of comment to use in requests
      "child": {}  - empty if number = 0
    },
    "1": {
      "level": 1,
      "number": 1, - number of child comments for use in cycle
      "author": "name2", - author name
      "text": "text of comment 2", - text
      "id": 2,     - ID of comment to use in requests
      "child": {
        "level": 2,
        "number": 0, - number of child comments for use in cycle
        "author": "anon3", - author name
        "text": "text of comment 3", - text
        "id": 3,     - ID of comment to use in requests
        "child": {}  - empty if number = 0
        }     
      }
  }
}

- get comments for Comment with depth
POST
url: http://127.0.0.1:8000/api/comment/8/comments/
where 8 in URL is ID of Comment
JSON body params:
"max_level" - int param, mean depth of comments tree, set 0 - for all child comments

return:
JSON
the tree of JSON is the same of previous request JSON response
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
