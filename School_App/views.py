from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import *

# Create your views here.

def home(request):
    return render(request, 'login_page/home.html')

def studentLogin(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        id = request.POST.get('password')
        class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

        for class_name in class_names:
            try:
                student_class = globals()[class_name]
                student = student_class.objects.get(Student_Name=name, Student_Id=id)
                return redirect('studentPage', student_name=student.Student_Name)
            except student_class.DoesNotExist:
                continue

        return render(request, 'login_page/studentLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login_page/studentLogin.html')


def parentRegistration(request):
    return render(request, 'login_page/parentRegister.html')

def teacherLogin(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        id = request.POST.get('password')
        try:
            teacher = Teachers_Info.objects.get(Name=name, STS_Teacher_Id=id)
            return redirect('teacherPage', teacher_name=teacher.Name)
        except Teachers_Info.DoesNotExist:
            return render(request, 'login_page/TeacherLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login_page/TeacherLogin.html')

def get_student_data(class_name, student_name):
    try:
        student_class = globals()[class_name]
        student = student_class.objects.get(Student_Name=student_name)
        return student
    except student_class.DoesNotExist:
        return None

def studentPage(request, student_name):
    class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

    for class_name in class_names:
        student_data = get_student_data(class_name, student_name)
        if student_data:
            return render(request, 'student_page/studentHome.html', {'student': student_data})

    return render(request, 'error_page.html', {'error_message': 'Student not found'})

def studentClass(request, student_name):
    class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

    for class_name in class_names:
        student_data = get_student_data(class_name, student_name)
        if student_data:
            return render(request, 'student_page/studentClass.html', {'student': student_data})

    return render(request, 'error_page.html', {'error_message': 'Student not found'})

def studentTimeTable(request, student_name):
    class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

    for class_name in class_names:
        student_data = get_student_data(class_name, student_name)
        if student_data:
            return render(request, 'student_page/studentTimeTable.html', {'student': student_data})

    return render(request, 'error_page.html', {'error_message': 'Student not found'})

def studentWork(request, student_name):
    class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

    for class_name in class_names:
        student_data = get_student_data(class_name, student_name)
        if student_data:
            detail = student_Work.objects.all()
            return render(request, 'student_page/studentWork.html', {'details': detail, 'student': student_data})

    return render(request, 'error_page.html', {'error_message': 'Student not found'})

def uploadWork(request, student_name):
    class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

    for class_name in class_names:
        student_data = get_student_data(class_name, student_name)
        if student_data:
            return render(request, 'student_page/workUpload.html', {'student': student_data})

    return render(request, 'error_page.html', {'error_message': 'Student not found'})



def upload(request):
    if request.method == 'POST':
        student_name = request.POST.get('name')
        student_class = request.POST.get('class')
        student_id = request.POST.get('studentId')
        subject_name = request.POST.get('subjectName')
        file_name = request.POST.get('fileName')
        file_uploaded = request.FILES.get('file')

        obj = student_Work(
            studentName=student_name,
            studentClass=student_class,
            studentId=student_id,
            subjectName=subject_name,
            fileName=file_name,
            file=file_uploaded
        ) 
        obj.save()

        return render(request, 'student_page/success.html')


def studentProfile(request, student_name):
    class_names = ['Class_one', 'Class_two', 'Class_three', 'Class_four', 'Class_five', 'Class_six', 'Class_seven']

    for class_name in class_names:
        try:
            student_class = globals()[class_name]
            student_data = student_class.objects.get(Student_Name=student_name)
            return render(request, 'student_page/studentProfile.html', {'student': student_data})
        except student_class.DoesNotExist:
            continue

    return render(request, 'error_page.html', {'error_message': 'Student not found'})


def teacherPage(request, teacher_name):
    data = Teachers_Info.objects.get(Name=teacher_name)
    return render(request, 'teacher_page/_teacherHome.html', {'teacher': data})
 
def teacherClass(request, teacher_name):
    return render(request, 'teacher_page/_teacherClass.html', {'teacher_name': teacher_name})

def teacherTimeTable(request, teacher_name):
    return render(request, 'teacher_page/_teacherTimeTable.html', {'teacher_name': teacher_name})

def teacherProfile(request, teacher_name):
    data = Teachers_Info.objects.get(Name=teacher_name)
    return render(request, 'teacher_page/_teacherProfile.html', {'teacher': data})


def teacherWork(request, teacher_name):
    return render(request, 'teacher_page/_studentClasses.html', {'teacher_name': teacher_name})

def class1(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='Class - 1')
    return render(request, 'class_page/class1.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def class2(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='Class - 2')
    return render(request, 'class_page/class2.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def class3(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='class-3')
    return render(request, 'class_page/class3.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def class4(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='class-4')
    return render(request, 'class_page/class4.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def class5(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='class-5')
    return render(request, 'class_page/class5.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def class6(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='class-6')
    return render(request, 'class_page/class6.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def class7(request, teacher_name):
    studentWorks = student_Work.objects.filter(studentClass='class-7')
    return render(request, 'class_page/class7.html', {'studentWorks':studentWorks,'teacher_name': teacher_name})

def addComment(request,id,teacher_name):
    myData = student_Work.objects.get(id=id)
    data = Teachers_Info.objects.get(Name=teacher_name)
    return render(request, 'teacher_page/_addComment.html', {'data':myData,'teacher_name': teacher_name, 'teacher': data})

def uploadComment(request,id):
    myData = student_Work.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        staffName = request.POST.get('staffName')
        myData.comment = comment
        myData.staffName = staffName
        myData.save() 
        return render(request, 'student_page/success.html')
    
def blog(request):
    data = student_Work.objects.all()
    return render(request, 'blog/blog.html', {'datas':data})

def game(request):
    return render(request, 'game/game.html')