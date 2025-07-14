from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Shortcut(BaseModel):
    title = models.CharField(max_length=255,null=False,blank=False,default="")
    shortcut = models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return self.title

class Function(BaseModel):
    title = models.CharField(max_length=255,null=False,blank=False,default="")
    function = models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return self.title

class Article(BaseModel):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,null=False,blank=False)
    short_desc = models.CharField(max_length=255,null=False,blank=False)
    description = models.TextField()
    shortcuts = models.ManyToManyField(Shortcut,blank=True)
    functions = models.ManyToManyField(Function,blank=True)
    
    def __str__(self):
        return self.title