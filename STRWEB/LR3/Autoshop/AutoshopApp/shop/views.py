from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import F, Q
import tzlocal
import datetime as dt
import calendar
import requests
import statistics
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from io import BytesIO
import base64
from django.http import JsonResponse
from datetime import date
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.base import ContentFile

@login_required
def profile_view(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-date')
    response = requests.get("https://favqs.com/api/qotd")
    quote = None

    if response.status_code == 200:
        data = response.json()
        quote = data['quote']['body']
    return render(request, 'profile.html', {'user': request.user, 'orders': user_orders,
                                            'profile' : Profile.objects.get(user=request.user), 'quote' : quote, 
                                            'max' : date.today().isoformat()})

def main(request):
    new = News.objects.last()
    timezone.activate(tzlocal.get_localzone())
    tz = timezone.get_current_timezone()
    cal = calendar.TextCalendar()
    
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    
    joke = ""
    if response.status_code == 200:
        data = response.json()
        joke = data.get("joke", "No joke found.")
    else:
        joke = "Failed to get a joke."
        
    search_query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', 'price')

    products = Product.objects.all()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(article__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    if sort_option in ['price', '-price', 'name', '-name']:
        products = products.order_by(sort_option)

    categories = ProductCategory.objects.prefetch_related(
        models.Prefetch(
            'product_set',
            queryset=products
        )
    ).all()

    partners = Partner.objects.all()

    return render(request, 'main.html', {
        'categories': categories,
        'news': new,
        'tz': tz,
        'date': timezone.now(),
        'cal': cal.formatmonth(2025, 5),
        'joke': joke,
        'search_query': search_query,
        'sort_option': sort_option,
        'partners': partners,
    })


def show_stats(request):
    if request.user.is_staff:
        ages = list(Profile.objects.values_list('age', flat=True))
        average_age = sum(ages) / len(ages) if ages else 0
        median_age = statistics.median(ages) if ages else 0

        plt.figure(figsize=(8, 4))
        plt.bar(range(1, len(ages)+1), ages, color='skyblue')
        plt.axhline(average_age, color='red', linestyle='--', label=f'Avarage: {average_age:.2f}')
        plt.axhline(median_age, color='green', linestyle=':', label=f'Median: {median_age}')
        plt.xlabel('Users')
        plt.ylabel('Age')
        plt.title('Users age')
        plt.legend()

        buffer = BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        age_chart = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        plt.close()

        age_context = {
            'average_age': average_age,
            'median_age': median_age,
            'chart': age_chart,
        }

        order_totals = []
        for order in Order.objects.all():
            total = sum(item.get_total_price() for item in order.order_items.all())
            order_totals.append(float(total))

        if not order_totals:
            return render(request, 'stats.html', {
                'age_context': age_context,
                'order_context': {'no_data': True}
            })

        avg = sum(order_totals) / len(order_totals)
        med = statistics.median(order_totals)
        try:
            moda = statistics.mode(order_totals)
        except statistics.StatisticsError:
            moda = "no mode"

        bins = {
            '<20': 0,
            '20–50': 0,
            '50–100': 0,
            '>100': 0,
        }

        for total in order_totals:
            if total < 20:
                bins['<20'] += 1
            elif total < 50:
                bins['20–50'] += 1
            elif total < 100:
                bins['50–100'] += 1
            else:
                bins['>100'] += 1

        plt.figure(figsize=(6, 6))
        plt.pie(bins.values(), labels=bins.keys(), autopct='%1.1f%%', startangle=90)
        plt.title('Orders by cost')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        order_chart = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        plt.close()

        order_context = {
            'average': avg,
            'median': med,
            'mode': moda,
            'chart': order_chart,
            'no_data' : False,
        }

        return render(request, 'stats.html', {
            'age_context': age_context,
            'order_context': order_context
        })

    return redirect('main')


def create_feedback(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FeedbackForm(request.POST) 
            feedback = form.save() 
            return redirect('reviews') 

        else:
            username = {}
            username['username'] = request.user.username
            form = FeedbackForm(initial=username)
    
    else:
        return redirect('login')
        
    return render(request, 'feedback.html', {'form': form})

def add_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST)
            if (form.is_valid()):  
                product = form.save()
                return redirect('viewproducts')
        else:
            form = AddProductForm()
    else:
        return redirect('main')
    
    return render(request, 'addproduct.html', {'form': form})


def add_provider(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProviderForm(request.POST)
            if (form.is_valid()):  
                product = form.save()
                return redirect('viewproviders')
        else:
            form = AddProviderForm()
    else:
        return redirect('main')
    
    return render(request, 'addprovider.html', {'form': form})

def show_products(request):
    if request.user.is_authenticated and request.user.is_superuser:
        prods = Product.objects.all()
        for prod in prods:
            prod.utc_created = prod.created.astimezone(datetime.timezone.utc)
        return render(request, 'viewproducts.html', {'prods' : prods})
    return redirect('main')

def delete_product(request, prod_id):
    if request.user.is_authenticated and request.user.is_superuser:
        item = get_object_or_404(Product, id=prod_id)
        item.delete()
        return redirect('viewproducts')
    return redirect('main')

def delete_provider(request, pr_id):
    if request.user.is_authenticated and request.user.is_superuser:
        item = get_object_or_404(Provider, id=pr_id)
        item.delete()
        return redirect('viewproviders')
    return redirect('main')

def edit_product(request, prod_id):
    if request.user.is_authenticated and request.user.is_superuser:
        item = get_object_or_404(Product, id=prod_id)
        if request.method == 'POST':
            form = AddProductForm(request.POST)
            if (form.is_valid()):    
                item.delete()
                feedback = form.save() 
                return redirect('viewproducts') 

        else:
            data = {}
            data['name'] = item.name
            data['article'] = item.article
            data['in_stock'] = item.in_stock
            data['price'] = item.price
            data['providers'] = item.providers.all()
            data['category'] = item.category
            form = AddProductForm(initial=data)
    
    else:
        return redirect('main')
        
    return render(request, 'editproduct.html', {'form': form})

def edit_provider(request, pr_id):
    if request.user.is_authenticated and request.user.is_superuser:
        item = get_object_or_404(Provider, id=pr_id)
        if request.method == 'POST':
            form = AddProviderForm(request.POST)
            if (form.is_valid()):
                item.delete()
                feedback = form.save() 
                return redirect('viewproviders') 

        else:
            data = {}
            data['name'] = item.name
            data['address'] = item.address
            data['phone_number'] = item.phone_number
            form = AddProviderForm(initial=data)
    
    else:
        return redirect('main')
        
    return render(request, 'editprovider.html', {'form': form})

def show_orders(request):
    if request.user.is_authenticated and request.user.is_staff:
        orders = Order.objects.all()
        return render(request, 'vieworders.html', {'orders' : orders})
    
    return redirect('main')

def show_providers(request):
    if request.user.is_authenticated and request.user.is_staff:
        providers = Provider.objects.all()
        d = timezone.now() - timezone.localtime()
        for p in providers:
            p.utc_created = p.created.astimezone(dt.timezone.utc)
        return render(request,'viewproviders.html', {'providers' : providers})
    
    return redirect('main')

def show_reviews(request):
    feedbacks = Feedback.objects.all()
    
    return render(request, 'reviews.html', {'feedbacks': feedbacks})

def show_about(request):
    info = get_object_or_404(AboutCompany)
    history_list = info.history.split('\n')
    return render(request, 'about.html', {'info' : info, 'history' : history_list})

def show_news(request):
    news = News.objects.all()
    
    return render(request, 'news.html', {'news': news})

def show_one_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    return render(request, 'one_news.html', {'news' : news})

def show_qa(request):
    qas = QandA.objects.all().order_by('-date')
    
    return render(request, 'qa.html', {'qa': qas})

def show_policies(request):
    return render(request, 'policies.html')

def show_promocodes(request):
    proms = Promocode.objects.all().order_by('-valid')
    return render(request, 'promocodes.html', {'promocodes' : proms})

def show_contacts(request):
    cont = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts' : cont})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def view_pickup(request):
    pick = PickPoints.objects.all()
    return render(request, 'pickups.html', {'picks' : pick})

@login_required
def view_cart(request):
    order, created = Order.objects.get_or_create(user=request.user, completed=False)

    cart_items = order.order_items.select_related('product').all()

    total_price = sum(item.get_total_price() for item in cart_items)

    return render(request, 'cart.html', {
        'cart': order,
        'cart_items': cart_items,
        'total_price': total_price
    })
    
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    order, created = Order.objects.get_or_create(user=request.user, completed=False)

    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'price_at_order': product.price, 'quantity': 1}
    )

    if not created:
        order_item.quantity = F('quantity') + 1
        order_item.save()

    Product.objects.filter(pk=product_id).update(in_stock=F('in_stock') - 1)

    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user, order__completed=False)
    
    Product.objects.filter(pk=item.product.id).update(in_stock=F('in_stock') + item.quantity)
    
    item.delete()
    return redirect('cart')

@login_required
def remove_one_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user, order__completed=False)
    
    Product.objects.filter(pk=item.product.id).update(in_stock=F('in_stock') + 1)
    
    if item.quantity == 1:
        item.delete()
    else:
        item.quantity = item.quantity - 1
        item.save()
    return redirect('cart')

@login_required
def checkout(request):
    try:
        order = Order.objects.get(user=request.user, completed=False)
        order.completed = True
        order.save()
    except Order.DoesNotExist:
        pass 

    return render(request, 'checkout.html')

def show_vacancy(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancies' : vacancies})

def show_one_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, 'one_product.html', {'product' : product})


def update_age(request):
    if request.method == "POST":
        date_str = request.POST.get("age") 
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        except:
            return JsonResponse({"message": "Invalid date"}, status=400)

        profile = request.user.profile
        profile.age = date_obj
        profile.save()

        return JsonResponse({"message": "Date updated successfully"})

    return JsonResponse({"message": "Invalid request"}, status=405)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def contacts_json(request):

    if request.method == "GET":
        cont = Contact.objects.all()
        data = []
        for c in cont:
            data.append({
                "id": c.id,
                "name": c.name,
                "description": c.description,
                "phone_number": c.phone_number,
                "email": c.email,
                "image": request.build_absolute_uri(c.image.url) if c.image else ""
            })
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        image_url = request.POST.get("image")   
        if not all([name, description, phone_number, email]):
            return JsonResponse({"error": "Missing fields"}, status=400)

        contact = Contact.objects.create(
            name=name,
            description=description,
            phone_number=phone_number,
            email=email
        )

        if image_url:
            try:
                headers = {
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"
                    )
                }
                response = requests.get(image_url, headers=headers, timeout=5)
        
                if response.status_code == 200:
                    filename = image_url.split("/")[-1]
                    contact.image.save(filename, ContentFile(response.content), save=True)
        
            except Exception as e:
                print("Image download error:", e)


        return JsonResponse({
            "id": contact.id,
            "name": contact.name,
            "description": contact.description,
            "phone_number": contact.phone_number,
            "email": contact.email,
            "image": request.build_absolute_uri(contact.image.url) if contact.image else ""
        })