from django.db import models
from login_app.models import User
       
class BookManager(models.Manager):
    def basic_validator(self, postData, user_id):
        errors = {}

        if not postData['title']:
            errors['title'] = "Title is required."
        elif len(postData['title']) < 1:
            errors['title'] = "Title should be at least 1 characters."

        if not postData['description']:
            errors['description'] = "Description is required."
        elif len(postData['description']) < 5:
            errors['description'] = "Description should be at least 5 characters."

        if not user_id:
            errors['uploaded_by'] = "Name of uploader is required."

        return errors

    def create_book(self,postData, user_id):
        return self.create(
            title=postData["title"],
            description=postData["description"],
            uploaded_by_id=user_id, 
            users_who_like_id=user_id,
        )    

class Book(models.Model):
    # id INT
    title = models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User,related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BookManager()

    def __str__(self):
        return f'{self.title}'

