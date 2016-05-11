from __future__ import unicode_literals

import datetime
from django.db import models
from masters.models import Kid, Adult
from django.utils import timezone
from smart_selects.db_fields import GroupedForeignKey


# Create your models here.
class Fund(models.Model):
    adult_id = models.ForeignKey(Adult, on_delete=models.CASCADE)
    kid_id = GroupedForeignKey(Kid,'adult_id',blank=True, null=True)
    Promise_of_Faith_No_of_Seats = models.CharField ("Promise of Faith No of Seats", max_length=3)
    Promise_of_Faith_Period = models.CharField("Promise of Faith Period", max_length=3)
    #Promise_of_Faith_Status = models.CharField("Promise of Faith Status", max_length=10)
    Promise_of_Faith_Total = models.DecimalField("Promise of Faith Total", max_digits=8, decimal_places=2)
    
    class Meta:
        ordering = ["adult_id"]
        verbose_name_plural = "fund"
        
    def __str__(self):
        return self.Promise_of_Faith_No_of_Seats
        
class Fpayment(models.Model):
	fund_id = models.ForeignKey(Fund, on_delete=models.CASCADE)
	Payment_of_period = models.CharField("Payment of period", max_length=4)
	Payment_of_value = models.DecimalField("Payment of value", max_digits=6, decimal_places=2)
	
	
	class Meta:
	    ordering = ["fund_id"]
	    verbose_name_plural = "fpayment"
	    
	def adult_name(self):
	    return self.fund_id.adult_id.first_name+ ' ' + self.fund_id.adult_id.last_name
	    
	#adult_name.admin_order_field = 'adult_id__first_name'	
	
	
	def kid_name(self):
	    try:
	        return self.fund_id.kid_id.first_name + ' ' + self.fund_id.kid_id.last_name
	    except Exception, e : 
	        return "-"
	        
	
	def __str__(self):
	    return self.Payment_of_period     