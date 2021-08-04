from django.db import models

def addComments(article, parent_id, level, author, text):
    """Add comment"""
    comment = Comment()
    comment.artcle = article
    comment.parent = parent_id
    if author != "":
        comment.author = author
    comment.level = level + 1
    comment.text = text
    comment.save()
    return comment.id

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField()

    def addArticle(self, title, text):
        self.title = title
        self.text = text
        self.save()

    def addComment(self, article_id, parent_id, level, author, text):
        """
        Add comment to article, which haven't parent comment.
        """
        return addComments(self, 0, level, author, text)

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    artcle = models.ForeignKey(Article, on_delete=models.PROTECT)
    parent = models.IntegerField()
    author = models.CharField(max_length=32, null=True, blank=True)
    level = models.IntegerField()
    text = models.TextField()

    def addComment(self, article_id, parent_id, level, author, text):
        """
        Add comment to article, which have parent comment.
        """
        return addComments(self.artcle, self.id, self.level, author, text)
