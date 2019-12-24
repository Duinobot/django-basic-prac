import datetime
from django.db.models import *

# Create your models here.
class Phone(Model):
    imei = CharField(max_length=128,unique=True)
    
    full_name = CharField(max_length=128)
    model = CharField(max_length=128)
    storage = CharField(max_length=128)
    color = CharField(max_length=128)
    grade = CharField(max_length=128)
    product_id = CharField(max_length=128)
    
    date_in = DateTimeField(default = datetime.datetime.now())
    date_out = DateTimeField()
    date_modified = DateTimeField(default = datetime.datetime.now())
    change_checked = BooleanField(default = False)
        
    input_confirmed = BooleanField(default = False)
    class Meta:
        db_table = "phones"
        
    def __str__(self):
        return self.model + ": " + self.imei