from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Question(models.Model):
    question = models.TextField(db_index=True)
    slug = models.SlugField(max_length=50, unique=True, blank = True)
    #category = models.ForeignKey('Category', blank = True, null=True,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.question[:100])

        super(Question, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.question}"

class Answer(models.Model):
    answer = models.TextField(blank=True, null=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)


class Test(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank = True)
    questions = models.ManyToManyField('Question', related_name='tests')


    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Test, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('testing:test_detail_url', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title


class TestRun(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    started = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now=True)
