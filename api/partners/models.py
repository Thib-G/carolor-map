from django.contrib.gis.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name = 'catégorie'
        verbose_name_plural = 'catégories'

    name = models.CharField('catégorie', max_length=255)

    def __str__(self):
        return self.name

class Partner(models.Model):

    class Meta:
        verbose_name = 'partenaire'
        verbose_name_plural = 'partenaires'

    name = models.CharField('nom', max_length=255)
    address = models.CharField('adresse', max_length=255)
    streetnumber = models.CharField('numéro', max_length=255)
    postcode = models.IntegerField('code postal')
    city = models.CharField('commune', max_length=255)
    phone = models.CharField('téléphone', max_length=255, null=True)
    url = models.URLField('Site web', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # GeoDjango specific field
    geom = models.PointField('géométrie')

    def __str__(self):
        return self.name
