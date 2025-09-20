from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie


User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_movie')
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas'),
        MaxValueValidator(5, 'A avaliação não pode ser superior a 5 estrelas')
        ]
    )
    comment = models.TextField(max_length=300)