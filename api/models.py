from django.db import models
from django.db.models import Sum
class CustomerCard(models.Model):
    customer=models.CharField(max_length=100)
    phone=models.IntegerField()
    vehicle_number=models.CharField(max_length=100)
    kilometers=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to="vehicle_images")
    status=models.CharField(max_length=100,default="pending")
    added_date=models.DateField(auto_now_add=True)


    
    @property
    def services(self):
            qs=Service.objects.filter(Customer_card=self)
            print(qs)
            return qs
    
    @property
    def total_amount(self):
         total=self.services.values('amount').aggregate(total=Sum('amount'))['total']
         print(total)
         return total


class Service(models.Model):
    title=models.CharField(max_length=100)
    notes=models.CharField(max_length=500)
    amount=models.IntegerField()
    Customer_card=models.ForeignKey(CustomerCard,on_delete=models.CASCADE)