from django.db import models


# Create your models here.
class Token(models.Model):
    '''
    存储access_token,和失效时间，以便确定是否要重新获取access_token
    '''
    access_token = models.CharField(max_length=255)
    end_time = models.DateTimeField()

    def __str__(self):
        return "(Token:{access_token:'%s', end_time:'%s'})" % (self.access_token, self.end_time)
