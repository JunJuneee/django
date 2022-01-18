from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Customer(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(
        max_length=10, choices=(('M', 'Male'), ('F', 'Femail')))
    created_by = models.ForeignKey(
        User, related_name='created_by',  editable=False, on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=10, choices=(
        ('draft', 'Draft'), ('published', 'Published')), default='draft')

    objects = models.Manager()

    # Customer.objects.filter(status='published')
    # Customer.published.all() 으로 간편하게 사용 가능
    published = PublishedManager()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)
