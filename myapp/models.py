from django.db import models
# Create your models here.

# 商品資料表(商品名稱,價格,圖片路徑,介紹)
class ProductModel(models.Model):
    pname = models.CharField(max_length=30, null=False)
    pprice = models.IntegerField(null=False)
    pimage = models.CharField(max_length=40, null=False)
    pdescription = models.TextField(null=False)