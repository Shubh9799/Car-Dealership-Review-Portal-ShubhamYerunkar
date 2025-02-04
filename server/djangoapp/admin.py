from django.contrib import admin  # type: ignore
from .models import CarMake, CarModel  # Correct import statement


# CarModelInline class to display CarModel within CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to show by default


# Class to customize CarModel in the admin interface
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make',
                    'type', 'year')  # Fields to display in the list view
    search_fields = ('name',
                     'car_make__name')  # Fields to be searchable
    list_filter = ('type',
                   'year', 'car_make')  # Filters for the list view


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'description')
    search_fields = ('name',)  # Fields to be searchable
    # Display related CarModel instances in CarMake admin page
    inlines = [CarModelInline]


# Register models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
