from django.db import models
from ..account.models import User
# Create your models here.


class Story(models.Model):
    name = models.CharField(max_length=45)
    body = models.TextField()
    image = models.CharField(max_length=255)
    rating = models.FloatField()
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zip_code = models.IntegerField()
    gps_x = models.FloatField()
    gps_y = models.FloatField()
    rating = models.FloatField()
    story = models.ForeignKey(Story)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Journey(models.Model):
    single_story = 'SS'
    journey_story = 'JS'
    story_type_choices = (
        (single_story, 'Single Story'),
        (journey_story, 'Journey Story')
    )
    name = models.CharField(max_length=45)
    body = models.TextField()
    journey_type = models.CharField(max_length=2, choices=story_type_choices, default=single_story)
    avg_genre = models.FloatField()
    story = models.ForeignKey(Story)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Journey_Feedback(models.Model):
    body = models.TextField()
    rating = models.FloatField()
    journey = models.ForeignKey(Journey)
    user = models.ForeignKey(Story)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Story_Feedback(models.Model):
    body = models.TextField()
    rating = models.FloatField()
    story = models.ForeignKey(Story)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
