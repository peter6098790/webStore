from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import ProductModel
# Create your views here.


cartlist = [] #購物車內容
shipping = 100 #運費

def index(request):
    products = ProductModel.objects.all()
    return render(request, 'index.html', locals())

def detail(request, id=None):
    product = ProductModel.objects.get(id = id)
    return render(request, 'detail.html', locals())

def addtocart(request, type=None,  id=None):
    global cartlist
    #add / update / empty / remove
    if type == 'add':
        product = ProductModel.objects.get(id = id)
        noCartSession = True
        #購物車中無商品
        #unit(商品名, 單價, 數量, 總價)
        for unit in cartlist:
            if product.pname == unit[0]:
                unit[2] = str(int(unit[2])+1)
                unit[3] = str(int(unit[3])+product.pprice*1)
                noCartSession = False
        #購物車中已有商品
        if noCartSession:
            templist=[]
            #(商品名, 單價, 數量, 總價)
            templist.append(product.pname)
            templist.append(str(product.pprice))
            templist.append(str(1))
            templist.append(str(product.pprice*1))
            cartlist.append(templist)
        request.session['cartlist'] = cartlist
        #print(request.session['cartlist'])
        return redirect('/cart/')
    elif type == 'empty':
        cartlist = []
        request.session['cartlist'] = cartlist
        return redirect('/cart/')
    elif type == 'update':
        if request.method == 'POST':
            counter = 1
            for unit in cartlist:
                unit[2] = request.POST.get('quantity'+str(counter), '1')
                unit[3] = str(int(unit[1])*int(unit[2]))
                counter += 1
            request.session['cartlist'] = cartlist
        return redirect('/cart/')
def cart(request):
    global cartlist
    global shipping
    localcartlist = cartlist
    localshipping = shipping
    total = 0

    for unit in cartlist:
        total += int(unit[3])
    totalPrice = total + localshipping #總價(購物車+運費)
    
    return render(request,'cart.html', locals())