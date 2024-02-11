from django.db import models

# Create your models here.
class Data(models.Model):
    tenant_id = models.TextField()
    account_id = models.TextField()
    device_id = models.TextField()
    device_name = models.TextField()
    rule_id = models.TextField()
    alarm_id = models.TextField()
    alarm_name = models.TextField()
    description = models.TextField()
    state = models.TextField()
    duration = models.TextField(null=True, blank=True)
    created_at = models.TextField()
    finalized_at = models.TextField(null=True, blank=True)
    severity = models.TextField()

    created = models.DateTimeField(auto_now_add=True)