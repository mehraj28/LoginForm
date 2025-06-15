from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def student_input_view(request):
    submitted= False
    sname= ''
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and printed the data")
            print('Name: ',form.cleaned_data['name'])
            print('Rollno: ', form.cleaned_data['rollno'])
            print('Marks: ',form.cleaned_data['marks'])
            sname= form.cleaned_data['name']
            submitted= True
    form = StudentForm()
    my_dict={'form': form,'submitted':submitted,'sname':sname}
    return render(request,'testapp/input.html',my_dict)