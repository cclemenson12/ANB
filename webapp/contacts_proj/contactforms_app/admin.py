from django.contrib import admin
#from django.utils.html import format_html_join
#from django.utils.safestring import mark_safe

# Register your models here.
from .models import contacts

#Commented out 10/23/20 to support mention below
#admin.site.register(contacts)

#Added 10/23/20 to enable seeing id field per https://stackoverflow.com/questions/47138660/show-object-id-primary-key-in-django-admin-object-page
class ContactsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(contacts, ContactsAdmin)
#admin.site.register(Contacts, ContactsAdmin)

#Added 10/4/20 to troubleshoot issue with migrations after making id field temporarily editable
#class ContactsAdmin(admin.ModelAdmin):
#    readonly_fields = ('id',)
#
#    def contacts_report(self, instance):
#        # assuming get_full_address() returns a list of strings
#        # for each line of the address and you want to separate each
#        # line by a linebreak
#        return format_html_join(
#            mark_safe('<br>'),
#            '{}',
#            ((line,) for line in instance.get_full_contact()),
#        ) or mark_safe("<span class='errors'>I can't determine this contact.</span>")
#
#    # short_description functions like a model field's verbose_name
#    contacts_report.short_description = "Contacts"
