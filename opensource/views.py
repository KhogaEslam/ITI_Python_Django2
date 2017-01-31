from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from models import student, track
from forms import student_form
# Create your views here.


#just print hello
def hello(request):
	return HttpResponse('helloooooo')


#show details
def details(request, st_id):
	st = student.objects.get(id=st_id)
	context = {'student_d': st}
	return render(request, 'opensource/student_details.html',context )


# list all
def show_all_students(request):
	all_st = student.objects.all()
	context = {'all_students': all_st}

	return render(request, 'opensource/index.html' ,context)


# create
def new_student(request):
	form = student_form()
	if request.method == 'POST':
		form = student_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/opensource/hello')

	context = {'st_form': form}
	return render(request, 'opensource/student_form.html',context )


# edit
def edit_student(request, st_id):
	
	st = student.objects.get(id= st_id)
	form = student_form(instance = st)
	if request.method == 'POST':
		form = student_form(request.POST, instance=st)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/opensource/hello')



	context = {'st_form': form}
	return render(request, 'opensource/student_form.html',context)




# delete 
def del_student(request, st_id):
	st = student.objects.get(id=st_id)
	st.delete()
	return HttpResponseRedirect('/opensource/hello')

