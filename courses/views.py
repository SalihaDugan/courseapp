from django.http import Http404
from django.shortcuts import  get_object_or_404, redirect, render

from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Categories, Course, UploadModel
from django.core.paginator import Paginator
import random
import os 

def index(request):
    # list comphension
    kurslar = Course.objects.filter(isActive = 1, isHome = 1)
    
    kategoriler = Categories.objects.all()
    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            # kurs = Course(title = form.cleaned_data["title"], 
            #               description = form.cleaned_data["description"],
            #               imageUrl = form.cleaned_date["imageUrl"],
            #               slug = form.cleaned_data["slug"])
            # kurs.save()

            form.save()
            return redirect("/kurslar")
        
    else:
        form = CourseCreateForm()   

    return render(request, "courses/create-course.html", {"form":form})

def course_list(request):
    kurslar = Course.objects.all()

    return render(request, 'courses/course-list.html', {
        'courses': kurslar
    })    

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.FILES, request.POST, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render(request, "courses/edit-course.html", {
        "form": form
    })

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)
    
    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course-delete.html", {
        "course": course
    })

# def upload(request):
#     if request.method == "POST":
#         uploaded_images = request.FILES.getlist("images")
#         for file in uploaded_images:
#             handle_uploaded_files(file)
#         return render(request, "courses/succes.html")

#     return render(request, "courses/upload.html")

# def upload(request):
#     if request.method == "POST":
#         form = UploadForm(request.POST, request.FILES)

#         if form.is_valid():
#             uploaded_image = request.FILES["image"]
#             handle_uploaded_files(uploaded_image)
#             return render(request, "courses/succes.html")
#     else:
#         form = UploadForm()
#     return render(request, "courses/upload.html", {"form": form})

# def handle_uploaded_files(file):
#     number = random.randint(1,99999)
#     # file_name _ 12222.jpg
#     filename, file_extention = os.path.splitext(file.name)
#     name = filename + "_" + str(number) + file_extention
#     with open("temp/" + name,"wb+") as destination:

#         for chunk in file.chunks():
#             destination.write(chunk)
    

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image = request.FILES["image"])
            model.save()
                        
            return render(request, "courses/succes.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {"form": form})


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter( isActive=True, title__contains=q).order_by("date")
        kategoriler = Categories.objects.all()
    else:
        return redirect("/kurslar")

    return render(request, 'courses/search.html' ,{

        'categories': kategoriler,
        'courses': kurslar,
            
    })


def details(request, slug):
    try:
        course = Course.objects.get(slug=slug)

    except:
        raise Http404()
    
    context = {
        'course': course
    }

    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug = slug, isActive=True).order_by("date")
    kategoriler = Categories.objects.all()

    paginator = Paginator(kurslar, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    print(paginator.count)
    print(paginator.num_pages)

    return render(request, 'courses/list.html' ,{

        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug,       
    })



# Create your views here.
