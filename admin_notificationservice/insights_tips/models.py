# models.py
from django.db import models
# from PushNotification1.models import NotificationSettings
from messages_notification.models import NotificationSettings
from django.utils import timezone

class AdminInsightsTips(models.Model):
    content_id = models.CharField(max_length=6, primary_key=True, unique=True, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=timezone.localtime)
    
    class Meta:
        db_table = 'admin_insights_tips'
        managed = True
    
    def __str__(self):
        return f'insights tips {self.content_id} created at {self.created_at}'
    
    def save(self, *args, **kwargs):
        if not self.content_id:
            last_content = AdminInsightsTips.objects.all().order_by('content_id').last()
            if last_content:
                last_id_num = int(last_content.content_id.replace('CON', ''))
                new_id_num = last_id_num + 1
            else:
                new_id_num = 1
            self.content_id = f'CON{new_id_num:03d}'
        super(AdminInsightsTips, self).save(*args, **kwargs)

class InsightsTipsNotifications(models.Model):
    notification_id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
    user_id = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'insights_tips_notifications'
    
    def __str__(self):
        return str(self.notification_id)
    
    def save(self, *args, **kwargs):
        # Ensure that each user has at most 5 notifications stored
        notifications_count = InsightsTipsNotifications.objects.filter(user_id=self.user_id).count()
        if notifications_count >= 5:
            oldest_notification = InsightsTipsNotifications.objects.filter(user_id=self.user_id).order_by('created_at').first()
            oldest_notification.delete()
    
        # Generate unique notification ID
        if not self.notification_id:
            last_notification = InsightsTipsNotifications.objects.all().order_by('notification_id').last()
            if last_notification:
                last_id_num = int(last_notification.notification_id.replace('NOTIT', ''))
                id_number = last_id_num + 1
            else:
                id_number = 1
            self.notification_id = f'NOTIT{id_number:05d}'
    
        super(InsightsTipsNotifications, self).save(*args, **kwargs)