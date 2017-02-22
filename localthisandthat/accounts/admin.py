# from django.contrib import admin
#
# # Register your models here.
# from .models import Profile
#
#
# # create class to customize admin
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ["first_name", "last_name", "email", "zip", "state", "city", "address_1", "address_2"]
#     list_display_link = ["timestamp"]
#     list_filter = ["first_name", "last_name", "email", "zip", "state", "city", "address_1", "address_2"]
#     list_editable = ["first_name", "last_name", "email", "zip", "state", "city", "address_1", "address_2"]
#     search_fields = ["first_name", "last_name"]
#
#     class Meta:
#         model = Profile
#
#
# # Registering the Post Model into admin site
# # and connects Post Model with PostModelAdmin
# admin.site.register(Profile, PostModelAdmin)