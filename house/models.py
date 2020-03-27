from django.db import models

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class House(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    rent = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    area = models.IntegerField()
    location = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    buildingFloor = models.IntegerField()
    floorLocation = models.IntegerField()
    furnished = models.CharField(max_length=10, choices=STATUS)
    balconied = models.CharField(max_length=10, choices=STATUS)
    heating = models.CharField(max_length=255)
    withintheSite = models.CharField(max_length=10, choices=STATUS)
    fromWho = models.CharField(max_length=255)

    def __str__(self):
        return self.title





