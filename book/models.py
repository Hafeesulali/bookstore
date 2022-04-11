from django.db import models


# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=120, unique=True)
    author = models.CharField(max_length=80)
    amount = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images", null=True)

    # created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book_name

# ORM
# ref=modelNAme(property=value,property=value,property=value)
# ref.save()

# qs=Books(books_name="aarachar",author="kr meera",amount="500",copies="45")
# qs.save()

# fetching all records
# refname=modelname.objects.all()
