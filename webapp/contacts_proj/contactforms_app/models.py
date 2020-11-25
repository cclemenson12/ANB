from django.db import models

# Create your models here.
import uuid
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
comm_pref_options = (
            ('E','Email'),
            ('M','Mail'),
            ('P','Phone'),
            ('T','Text Messages'),
            )

class contacts(models.Model):
    #id = models.AutoField()
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False) #id field not visible in admin with this syntax
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    fname = models.CharField(max_length=30,blank=True,verbose_name=_('First Name'))
    lname = models.CharField(max_length=30,blank=True,verbose_name=_('Last Name'))
    email = models.EmailField(blank=True,verbose_name=_('Email Address'))
    street_addr = models.CharField(max_length=50,blank=True,verbose_name=_('Street Address'))
    city = models.CharField(max_length=30,blank=True,verbose_name=_('City'))
    state = models.CharField(max_length=2,blank=True,verbose_name=_('State'))
    zip_code = models.CharField(max_length=30,blank=True,verbose_name=_('Zip Code'))
    phone = models.CharField(max_length=30,blank=True,verbose_name=_('Phone Number'))
    years_participated = models.IntegerField(blank=True,verbose_name=_('# of Years in Program'))
    project_updates = models.BooleanField(default=True, blank=True,verbose_name=_('Subscribe to Project Updates'),help_text="""Check if you would like to get updates about the Moorhead Brewers projects""")
    news_events = models.BooleanField(default=True, blank=True,verbose_name=_('Subscribe to Moorhead Brewers News'),help_text="""Check if you would like to get general news about our the Moorhead Brewers""")
    comm_pref = models.CharField(blank=True, choices=comm_pref_options,default='email',max_length=1,verbose_name=_('Communications Preference'),help_text="""Choose the method you would prefer the Moorhead Brewers use to contact you. Note: The Moorhead Brewers may use email as primary for some communications""")
    unsubscribe = models.BooleanField(default=False, blank=True,verbose_name=_('Unsubscribe to all Communications'),help_text="""Check if you wish to unsubscribe from all communications from the Moorhead Brewers""")
    created = models.DateTimeField(blank=True, auto_now_add=True)
    last_emailed = models.DateTimeField(blank=True, null=True)
    web_updated = models.BooleanField(default=False, blank=True)
    duplicate = models.BooleanField(default=False, blank=True)
    #def get_absolute_url(self):
    #    return reverse('contact_detail', kwargs={'slug': self.slug})
    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("contacts:contact-change", kwargs={"id": self.id})
