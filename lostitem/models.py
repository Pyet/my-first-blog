from django.db import models
from django.utils import timezone

"""Class for lost items"""
class ItemLost(models.Model):
    """attributes"""
    id = 0
    """creator = models.ForeignKey('auth.User')"""
    color = models.ForeignKey('Color')
    description = models.CharField(max_length=400)
    added_date = models.DateTimeField(
            default=timezone.now)
    where_was_found = models.CharField(max_length=200)
    where_is_stored = models.CharField(max_length=200)

    """methods"""
    def create(self):
        self.save()
    def __str__(self):
        return '[ id : ' + str(self.id) + ' description : ' + self.description + ' where was it found ? ' + self.where_was_found + ' ]'
    def getColor(self):
        return self.color.name
"""Class for colors"""
class Color(models.Model):
    """attributes"""
    id = 0
    name = models.CharField(max_length=50)

    """methods"""
    def create(self):
        self.save()
    def __str__(self) :
        return self.name
