from testAPI.models import Comment, Article
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def setParam(name, text, data):
    if name in data.keys():
        text = data[name]
    return text

def commentList(article_id, comment_id, level):
    if comment_id == 0:
        return Comment.objects.filter(artcle_id=article_id, level=level + 1)
    else:
        return Comment.objects.filter(artcle_id=article_id, parent=comment_id, level=level + 1)

def addCommentToDic(article_id, comment_id, number, comments, max_level):
    if comment_id == 0:
        for c in commentList(article_id, comment_id, comments["level"]):
            print(commentList)
            if c.level <= max_level or max_level == 0:
                comments["child"][str(comments["number"])] = {
                    "level": c.level,
                    "number": 0,
                    "child": {},
                    "author": c.author,
                    "text": c.text,
                    "id": c.id
                    }
                comments["child"][str(comments["number"])] = addCommentToDic(c.artcle, c.id, comments["number"], comments["child"][str(comments["number"])], max_level)
                comments["number"] += 1
    else:
        for c in commentList(article_id, comment_id, comments["level"]):
            if c.level <= max_level or max_level == 0:
                comments["child"][str(comments["number"])] = {
                    "level": c.level,
                    "number": 0,
                    "child": {},
                    "author": c.author,
                    "text": c.text,
                    "id": c.id
                    }
                comments["child"][str(comments["number"])] = addCommentToDic(c.artcle, c.id, comments["number"], comments["child"][str(comments["number"])], max_level)
                comments["number"] += 1
    return comments

@csrf_exempt
def api_getCommentsByArticle(request, pk):
    """
    if all arguments > 0 get comments with parent comment ID = comment_id and
        article ID = article_id and max max_level
    if comment_id = 0 and max_level = 0 get all comments to article
    if comment_id != 0 and max_level = 0 get all comments to comments
    if comment_id = 0 and max_level > 0 get all comments with level <= max_level
    """

    data = json.loads((request.body).decode('utf-8'))
    article_id = pk
    max_level = int(setParam("max_level", "3", data))

    return JsonResponse(addCommentToDic(pk, 0, 0, {"level":0, "number": 0, "child":{}}, max_level))

@csrf_exempt
def api_getCommentsByComment(request, pk):
    comment = Comment.objects.filter(id=pk).first()

    data = json.loads((request.body).decode('utf-8'))
    article_id = comment.artcle.id
    level = comment.level
    max_level = int(setParam("max_level", "3", data))

    return JsonResponse(addCommentToDic(article_id, pk, level, {"level":level, "number": 0, "child":{}}, max_level))

@csrf_exempt
def api_putArticle(request):
    data = json.loads((request.body).decode('utf-8'))
    article = Article()
    article.save()
    title = setParam("title", "title article " + str(article.id), data)
    text = setParam("article_id", "some text", data)

    article.addArticle(title, text)

    return JsonResponse({"status": "200", "article id": article.id})

@csrf_exempt
def api_putComment(request):
    data = json.loads((request.body).decode('utf-8'))
    author = setParam("author", "anonimous", data)
    text = setParam("text", "some text", data)
    parent_id = int(setParam("parent_id", 0, data))
    article_id = int(setParam("article_id", 0, data))
    if parent_id == 0:
        article = Article.objects.filter(id=article_id).first()
        id = article.addComment(article_id, parent_id, 1, author, text)
    else:
        comment = Comment.objects.filter(id=parent_id).first()
        id = comment.addComment(article_id, parent_id, comment.level + 1, author, text)

    return JsonResponse({"status": "200", "comment id": id})
