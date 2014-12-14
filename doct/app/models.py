from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, blank=False)
    link = models.CharField(max_length=512, blank=False)
    description = models.CharField(max_length=2048, blank=False)
    # key = models.CharField(max_length=512, blank=False)

    class Meta:
        managed = True
        db_table = 'Task'
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class StatTask(models.Model):
    task = models.OneToOneField(Task)
    update_time = models.DateTimeField(auto_now=False)
    number_users = models.IntegerField(default=0)
    number_teams = models.IntegerField(default=0)
    number_hosts = models.IntegerField(default=0)
    total_credit = models.FloatField(default=0)
    update_time_db = models.DateTimeField(auto_now=True)


class Contribute(models.Model):
    ram = models.PositiveIntegerField(default=1024, verbose_name='RAM')
    cpu = models.PositiveIntegerField(default=2, verbose_name='CPU (number of core)')
    # gpu = models.PositiveIntegerField(default=0, verbose_name='GPU')
    disk_space = models.IntegerField(default=1024, verbose_name='Disk pace (Mo)')
    # email = models.CharField()
    # password = models.CharField()




