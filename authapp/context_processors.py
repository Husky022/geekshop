from basket.models import Basket

def user_status(request):
    user = request.user
    if user.is_authenticated:
        status = '<h1>Авторизован</h1>'
    else:
        status = '<h1>Не авторизован</h1>'
    return {'status': status}

def basket_price(request):
    user = request.user
    if user.is_authenticated:
        price = f'В корзине на {Basket(user=user).total_sum()} руб.'
    else:
        price = 0
    return {'price': price}

def basket_count(request):
    user = request.user
    if user.is_authenticated:
        counter = Basket.objects.filter(user=user).count()
    else:
        counter = 0
    return {'basket_counter': counter}

