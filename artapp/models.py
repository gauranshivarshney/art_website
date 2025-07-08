from django.db import models

# Create your models here.
class Artwork(models.Model):
    tag = models.CharField(max_length=50, choices=[
        ("Mandala", "Mandala"),
        ("Strippling(Dotted)", "Strippling(Dotted)"),
        ("Oil Pastel", "Oil Pastel"),
        ("Color", "Color"),
        ("Other", "Other")
    ])
    image = models.ImageField(upload_to='artwork/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tag