from django.contrib import admin

from .models import student, track

# Register your models here.

class student_custom(admin.StackedInline):
	model = student
	extra = 5

class student_cutom_2(admin.ModelAdmin):
	list_display = ('st_name', 'st_age', 'st_track', 'is_born_before_1992')

	fieldsets = (
		['Personal Information', {'fields':['st_name', 'st_age']}],
		['Scholarship Information',{'fields':['st_track']} ]

		)
	search_fields = ['st_name', 'st_age']
	list_filter = ['st_track', 'st_age']



class track_custom(admin.ModelAdmin):
	inlines = [student_custom]



admin.site.register(student, student_cutom_2)
admin.site.register(track, track_custom)
