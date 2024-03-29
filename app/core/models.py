from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User


# TODO make the frequency model that can be changed

class Task(models.Model):
    '''
    defines tasks name , frequency, 
    '''
    options = {
        ('every_1m','Every min'),
        ('every_10m','Every 10 min'),
        ('every_30m','Every 30 min'),
        ('hourly', 'Hourly'),
        ('weekly', 'Weekly'),
        ('yearly', 'Yearly'),
    }
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True, blank=True)
    frequency = models.CharField(max_length=10, choices = options, default='hourly')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True,editable=False)


    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self)->str:
        return self.title


# scheduled tasks
class Schedule(models.Model):

    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, null=True, related_name='task_schedule')
    comment = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    interval = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    days_of_week = models.CharField(max_length=50, blank=True, null=True)
    months_of_year = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20)
    is_finished = models.BooleanField(default=False)
      
    class Meta:
        ordering=('due_date',)
      #  unique_together=('task', 'due_date','') # 

    def __str__(self) -> str:
        return self.task.title
    
class Assignment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.schedule.task.title} - {self.assignee.username} - {self.get_status_display()}" 

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('reminder', 'Reminder'),
        ('alert', 'Alert'),
    ]
    DELIVERY_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)
    notification_datetime = models.DateTimeField()
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_notification_type_display()} Notification for {self.assignment.schedule.task.title} to {self.recipient.username}"
    
    

