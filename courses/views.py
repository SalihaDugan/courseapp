from django.http import Http404
from django.shortcuts import  get_object_or_404, redirect, render

from courses.forms import CourseCreateForm, CourseEditForm
from .models import Categories, Course
from django.core.paginator import Paginator

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
        form = CourseCreateForm(request.POST)

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
        form = CourseEditForm(request.POST, instance=course)
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
