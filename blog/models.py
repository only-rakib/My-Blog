from django.db import models

class UvaSolve(models.Model):

    title = models.CharField(max_length=100)
    url_txt = models.URLField(max_length=200)
    description = models.TextField()
    critical_input = models.TextField()
    critical_output = models.TextField()
    code_txt = models.TextField()

    def __str__(self):
        return self.title