from datetime import date, datetime
from django.http import Http404,  HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Categories, Course
data = {
    "programlama": "programlama kategorisine ait kurslar",
    "web-gelistirme": "web geliştirme kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar",
}

db= {
    "courses": [
        {
            "title":"javascript kursu",
            "description": "javascript kurs açıklaması",
            "imageUrl": "1.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "2.jpg",
            "slug": "python-kursu",
            "date": date(2022,10,10),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "3.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2022,10,10),
            "isActive": True,
            "isUpdated": True
        },
    ],
    "categories": [
        {"id": 1, "name": "programlama", "slug":"programlama"}, 
        {"id": 2, "name": "web geliştirme", "slug":"web-gelistirme"},
        {"id": 3, "name": "mobil uygulamalar", "slug":"mobil-uygulamalar"},
        ]
}
# http://127.0.0.1:8000/kurslar


def index(request):
    # list comphension
    kurslar = Course.objects.filter(isActive = 1)
    
    kategoriler = Categories.objects.all()
    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
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

def getCoursesByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, "courses/courses.html", {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category])

    return redirect(redirect_url)

# Create your views here.
