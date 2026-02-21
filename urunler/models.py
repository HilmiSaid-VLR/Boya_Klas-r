from django.db import models

class Parca(models.Model):
    isim = models.CharField(max_length=200)
    resim = models.ImageField(upload_to='parcalar/', blank=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    aciklama = models.TextField(blank=True)

    def __str__(self):
        return self.isim

class Cihaz(models.Model):
    isim = models.CharField(max_length=200)
    resim = models.ImageField(upload_to='cihazlar/', blank=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    kisa_aciklama = models.CharField(max_length=300, help_text="Kartın üzerinde görünecek kısa yazı")
    detayli_aciklama = models.TextField(help_text="Pop-up içinde çıkacak detaylı bilgi")
    # İlişki: Bir cihazın birden fazla parçası olabilir
    parcalar = models.ManyToManyField(Parca, related_name='cihazlar', blank=True)

    def __str__(self):
        return self.isim
