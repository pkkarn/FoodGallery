from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self):
        return f"Title: {self.title}, Category: {self.category}"


