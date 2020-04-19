from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField()

    def summary(self):
        return self.content[:100]

    def __str__(self):
        return self.title
