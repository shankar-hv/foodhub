from django.shortcuts import render
from .models import FoodItem, Order
from django.shortcuts import redirect
from django.contrib.auth.models import User
# from .models import FoodItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    search = request.GET.get('search')
    
    if search:
        foods = FoodItem.objects.filter(
            name__icontains=search
        )
    else:
        foods = FoodItem.objects.all()

    context = {
        'foods': foods
    }

    return render(request, 'app/home.html', context)

@login_required
def about(request):
    return render(request, 'app/about.html')

@login_required
def contact(request):
    return render(request, 'app/contact.html')

@login_required
def food_detail(request, id):
    food = FoodItem.objects.get(id=id)

    context = {
        'food': food
    }

    return render(request, 'app/food_detail.html', context)

@login_required
def add_to_cart(request, id):
    cart = request.session.get('cart', [])
    cart.append(id)
    request.session['cart'] = cart
    
    return redirect('/cart/')

@login_required
def cart(request):
    cart = request.session.get('cart', [])

    foods = FoodItem.objects.filter(id__in=cart)

    total = 0

    for food in foods:
        total += food.price

    context = {
        'foods': foods,
        'total': total
    }

    return render(request, 'app/cart.html', context)

@login_required
def remove_from_cart(request, id):

    cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)

    request.session['cart'] = cart

    return redirect('/cart/')

def signup_page(request):

    if request.user.is_authenticated:
        return redirect('/home/')

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('/login/')

    return render(request, 'app/signup.html')

def login_page(request):

    if request.user.is_authenticated:
        return redirect('/home/')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/home/')

    return render(request, 'app/login.html')

def logout_page(request):

    logout(request)

    return redirect('/login/')

@login_required
def place_order(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    cart = request.session.get('cart', [])

    foods = FoodItem.objects.filter(id__in=cart)

    for food in foods:

        Order.objects.create(
            user=request.user,
            food_item=food
        )

    request.session['cart'] = []

    return render(request, 'app/order_success.html')

@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-ordered_at')

    context = {
        'orders': orders
    }

    return render(
        request,
        'app/my_orders.html',
        context
    )

@login_required
def profile(request):
    return render(request, 'app/profile.html')
