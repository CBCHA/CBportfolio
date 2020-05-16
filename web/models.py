from django.db import models

# Create your models here.
class PfItem(models.Model):
    objects = models.Manager()
    dfilter = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pfItem', blank=True)
    year = models.IntegerField(default=2020)
    month = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('dfilter', 'year', 'month', )
        verbose_name = 'pfItem'
        verbose_name_plural = 'pfItems'

    def __str__(self):
        return '{}'.format(self.name)

class FactItem(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    icon = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )
        verbose_name = 'factItem'
        verbose_name_plural = 'factItems'

    def __str__(self):
        return '{}'.format(self.name)

class BucketList(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    icon = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    attain = models.BooleanField()

    class Meta:
        ordering = ('name', )
        verbose_name = 'bucketList'
        verbose_name_plural = 'bucketLists'

    def __str__(self):
        return '{}'.format(self.name)
        
class MailBox(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    memo = models.TextField(blank=True)
    ip = models.CharField(max_length=20)

    class Meta:
        ordering = ('ip', )
        verbose_name = 'mailBox'
        verbose_name_plural = 'mailBoxes'

    def __str__(self):
        return '{}'.format(self.name)

class SkillList(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    scale = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        ordering = ('name', )
        verbose_name = 'skillList'
        verbose_name_plural = 'skillLists'

    def __str__(self):
        return '{}'.format(self.name)

class MapBadge(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    year = models.IntegerField(default=1991)
    image = models.ImageField(upload_to='mapBadge', blank=True)

    class Meta:
        ordering = ('year', )
        verbose_name = 'mapBadge'
        verbose_name_plural = 'mapBadges'

    def __str__(self):
        return '{}'.format(self.name)