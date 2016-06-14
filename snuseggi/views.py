from django.shortcuts import render
from .models import Restaurant
from .models import Assessment
from .models import Menu
from .parsing import menulist

# Create your views here.
def restaurants(request):
    restaurant_list = Restaurant.objects.all().order_by('name')
    return render(request, 'snuseggi/restaurants.html', {'restaurant_list' : restaurant_list})

def assessments(request):
    assessment_list = Assessment.objects.all().order_by('date')
    return render(request, 'snuseggi/assessments.html', {'assessment_list' : assessment_list})

# input : name of restaurant
def review_list(request):
    input='기숙사식당관악사(919동)'
    today_menus = menulist(input)

    point_of_menu = []
    starlist = ['☆☆☆☆☆', '★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
    for iter in range(0,3):
        current_menu = Menu.objects.filter(name=today_menus[iter])
        current_review_list = Assessment.objects.filter(menus=current_menu)

        sum_of_taste = 0
        for review_in_list in current_review_list:
            sum_of_taste = sum_of_taste + review_in_list.point_taste

        if len(current_review_list) == 0:
            point_of_menu.append('평가없음')
        else:
            point_of_menu.append(starlist[round(sum_of_taste / len(current_review_list))])

    return render(request, 'snuseggi/review_list.html', {'restaurant' : input, 'breakfast': today_menus[0], 'lunch' : today_menus[1],
                                                         'dinner' : today_menus[2], 'point_breakfast' : point_of_menu[0],
                                                         'point_lunch' : point_of_menu[1], 'point_dinner' : point_of_menu[2]})