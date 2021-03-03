from django.db import models

# Create your models here.


class Operation:
    def __init__(self, x, action, y, result):
        self.x = x
        self.action = action
        self.y = y
        self.result = result
