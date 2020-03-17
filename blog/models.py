from django.db import models

STATUS = (
    (1,"Zahozeno"),
    (0,"Publikováno")
)

class Novinky(models.Model):
    nazev = models.TextField()
    obsah = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    vytvoreno = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    foto = models.ImageField(blank=True, upload_to='images/')
    foto2 = models.ImageField(blank=True, upload_to='images/')
    foto3 = models.ImageField(blank=True, upload_to='images/')





    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.nazev
