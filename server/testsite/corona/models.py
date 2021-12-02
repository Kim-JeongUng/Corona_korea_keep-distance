from django.db import models
from django.urls import reverse


class User(models.Model):

    username = models.CharField(max_length=64,verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm=models.DateTimeField(auto_now=True,verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table='test_user'


class Event(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    class Meta:
        db_table='cal_user'
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))

        return f'<a href="{url}"> {self.title}</a>'




