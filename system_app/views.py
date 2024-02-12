from django.shortcuts import render, redirect
from datetime import datetime
import psycopg2
from .models import Feedback, Supplier, Customer, Product, Order, Stock

from django.http import HttpResponse
from django.views.generic import View
# importing get_template from loader
from django.template.loader import get_template
# import render_to_pdf from util.py
from .utils import render_to_pdf



conn = psycopg2.connect(
    database="erp_data", user='postgres', password='root'
# database="mydb", user='postgres', password='sneha123', host='127.0.0.1', port= '5432'
)


# Setting auto commit false

conn.autocommit = True

# Creating a cursor object using the cursor() method

cursor1 = conn.cursor()


# Create your views here.
def index(request):
    data = {}
    data['s_user'] = request.session.get('user')
    return redirect("home")

def signup(request):
    sign_data = {}    
    if request.method == "GET":
             return render(request, 'signup.html')
    else:
         c_fname = request.POST.get('sname')
         c_add = request.POST.get('sadd')
         c_no = request.POST.get('sno')
         c_mail = request.POST.get('smail')
         c_name = request.POST.get('user')
         c_pass = request.POST.get('s_pass')
         print(c_name,c_pass,c_add,c_mail,c_no,c_fname)
         cursor1 = conn.cursor()
         cursor1.execute("select * from customer where customer_user='" + c_name + "'")
         temp1 = cursor1.fetchall()
         rowcount1 = len(temp1)
         print(rowcount1) 
         if rowcount1 == 1:
            sign_data['msg'] = 'user allready exist'
            return render(request, 'signup.html', sign_data)
         else:
              savecard = Customer()
              savecard.customer_name = c_fname
              savecard.customer_address = c_add
              savecard.customer_contact = c_no
              savecard.customer_mail = c_mail                            
              savecard.customer_user = c_name
              savecard.customer_password = c_pass
              savecard.save()               
              return render(request, 'signup.html')                

def product_display(request):
    data = {}
    data['s_user'] = request.session.get('user')
    if request.method == "GET":
        showall = Product.objects.all()
        data['result'] = showall
        return render(request, 'product.html', data)
    else:
        if 'buy' in request.POST:
            pid = request.POST.get('p_id')
            request.session['pid'] = request.POST.get('p_id')
            data['p_id'] = request.session.get('pid')
            print(data['p_id'])
            if data['s_user'] == None:
                return redirect("log")
            else:
                return redirect("order")          

def profile(request):
    data = {}
    data['s_user'] = request.session.get('user')
    data['result'] = Customer.objects.filter(customer_user=data['s_user'])
    return render(request, 'profile.html', data)

def buy(request):
    data = {}
    data['s_user'] = request.session.get('user')
    data['p_id'] = request.session.get('pid')
    data['result'] = Customer.objects.filter(customer_user=data['s_user'])
    data['result1'] = Product.objects.filter(id=data['p_id'])
    if request.method == "GET":      
        return render(request, 'buy.html', data)
    else:
        name = request.POST.get('sname')
        addr = request.POST.get('sadd')
        no = request.POST.get('sno')
        c_user = request.POST.get('user')
        p_id = request.POST.get('cid')
        p_name = request.POST.get('pname')
        cost = request.POST.get('price')
        p_qty = request.POST.get('qty') 
        p_stock = request.POST.get('stock') 
        a = int(cost)
        b = int(p_qty)
        total = a * b
        c = int(p_stock)
        if b > c:
            data['msg'] = 'Invalid stock amount'
            return render(request, 'buy.html', data)
        else:
            stock = c - b
            up_stock = str(stock)
            date = datetime.today().strftime('%Y-%m-%d')            
            savecard = Order()
            savecard.customer_name = name
            savecard.customer_address = addr
            savecard.customer_mobile = no
            savecard.user_name = c_user
            savecard.product_id = p_id
            savecard.product_name = p_name
            savecard.product_price = cost
            savecard.product_Qty = p_qty    
            savecard.order_total = total 
            savecard.order_date = date                          
            savecard.save()
            data['c_name'] = name
            data['address']= addr
            data['contact']= no  
            data['p_name'] = p_name
            data['price']= cost
            data['qty']= p_qty 
            data['final'] = total 
            sql = "UPDATE product SET product_stock ='" + up_stock + "' where id='" + p_id + "'"
            cursor1.execute(sql)                     
            return render(request, 'place_order.html', data)
    
def order(request):
    data = {}
    data['s_user'] = request.session.get('user')
    data['p_id'] = request.session.get('pid')
    data['result'] = Customer.objects.filter(customer_user=data['s_user'])
    data['result1'] = Product.objects.filter(id=data['p_id'])
    if request.method == "GET":      
        return render(request, 'buy.html', data)

def my_order(request):
    data = {}
    data['s_user'] = request.session.get('user')
    data['result'] = Order.objects.filter(user_name=data['s_user'])
    if request.method == "GET":
        return render(request, 'orders.html', data)
    else:
        suname = request.POST.get('name')
        sadd = request.POST.get('add')
        mobile = request.POST.get('no')
        c_user = request.POST.get('user')
        prod = request.POST.get('p_name')
        cost = request.POST.get('price')
        p_qty = request.POST.get('qty')
        add = request.POST.get('total')
        od_date = request.POST.get('o_date')        
        print(suname,sadd,mobile,c_user)
        template = get_template('receipt.html')
        context = {
                "invoice_id": "recid",
                "customer_name": suname,
                "date": od_date,
                "address": sadd,
                "mobile": mobile,
                "user": c_user,
                "product": prod,
                "amount": cost,
                "qty": p_qty,
                "total": add                
            }
        html = template.render(context)
        pdf = render_to_pdf('receipt.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "User_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response                   
            return HttpResponse("Not found")

def feed(request):
    data = {}
    data['s_user'] = request.session.get('user')
    if request.method == "GET":
            return render(request, 'feedback.html', data)
    else:
         name = request.POST.get('fname')
         addr = request.POST.get('fmail')
         c_feed = request.POST.get('feed')
         print(name,addr,c_feed)
         savecard = Feedback()
         savecard.fullname = name
         savecard.email = addr
         savecard.feedback = c_feed
         savecard.save()
         return render(request, 'product.html')         

def login(request):
    data = {}
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        if 'log' in request.POST:
            name = request.POST.get('cuser')
            passw = request.POST.get('cpass')
            cursor = conn.cursor()
            cursor.execute("select * from customer where customer_user='" + name + "' and customer_password ='" + passw + "'")
            tempvar = cursor.fetchall()
            rowcount = len(tempvar)
            print(rowcount)

            if rowcount == 1:
                request.session['user'] = name
                data['s_user'] = request.session.get('user')
                print(request.session['user'])
                return redirect("home")
                # return render(request, 'product.html', data)

            else:
                data['msg'] = 'enter valid username or password'
                return render(request, 'login.html', data)
            
def logout(request):
    del request.session['user']
    return redirect('log')

def a_logout(request):
    del request.session['a_user']
    return redirect('a_log')

def admin_log(request):
    data = {}
    if request.method == "GET":
        return render(request, 'admin_log.html')
    else:
        if 's_log' in request.POST:
            name = request.POST.get('auser')
            passw = request.POST.get('apass')
            print(name,passw)
            if name == 'admin' and passw == 'admin123':
                request.session['a_user'] = name
                data['ad_user'] = request.session.get('a_user')
                print(request.session['a_user'])
                return redirect("stock")
            else:
                data['msg'] = 'enter valid username or password'
                return render(request, 'admin_log.html', data)

def ad_profile(request):
    showall = Customer.objects.all()
    data = {}
    data['ad_user'] = request.session.get('a_user')
    data['result'] = showall
    if request.method == "GET":
        return render(request, 'admin/customer_data.html', data)
    else:
        suname = request.POST.get('name')
        sadd = request.POST.get('add')
        smo = request.POST.get('mail')
        mobile = request.POST.get('no')
        c_user = request.POST.get('user')
        cu_pass = request.POST.get('c_pass')
        print(suname,sadd,smo,mobile,c_user,cu_pass)
        template = get_template('admin/user_receipt.html')
        context = {
                "invoice_id": "recid",
                "customer_name": suname,
                "address": sadd,
                "mobile": mobile,
                "mail": smo,
                "user": c_user,
                "passw": cu_pass
            }
        html = template.render(context)
        pdf = render_to_pdf('admin/user_receipt.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "User_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response                   
            return HttpResponse("Not found")

def ad_sup_profile(request):
    showall = Supplier.objects.all()
    data = {}
    data['ad_user'] = request.session.get('a_user')
    data['result'] = showall
    if request.method == "GET":
        return render(request, 'admin/supplier_data.html', data)
    else:
        if 'del' in request.POST:
            info = request.POST.get('en_del')
            cursor1.execute("delete from supplier where id ='" + info + "'")
            print(info)
            return redirect('as_data')
        elif 'search' in request.POST:
            name = request.POST.get('prod')
            print(name)
            data['result'] = Supplier.objects.filter(supplier_user=name)
            return render(request, 'admin/supplier_data.html', data)
    
def supply(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    if request.method == "GET":
        return render(request, 'admin/supplier.html', data)
    else:
         suname = request.POST.get('su_name')
         sadd = request.POST.get('su_add')
         smo = request.POST.get('su_no')
         smail = request.POST.get('su_mail')
         cname = request.POST.get('co_name')
         cadd = request.POST.get('co_add')
         cmail = request.POST.get('co_mail')
         bank = request.POST.get('cb_name')
         ano = request.POST.get('a_no')
         sname = request.POST.get('suser')
         spass = request.POST.get('spass')
         print(suname,sadd,smail,smo,cname,cadd,cmail,bank,ano)
         cursor1 = conn.cursor()
         cursor1.execute("select * from supplier where supplier_user='" + sname + "'")
         temp = cursor1.fetchall()
         rowcount = len(temp)
         print(rowcount)
         if rowcount == 1:
            data['msg'] = 'Supplier allready exist'
            return render(request, 'admin/supplier.html', data)
         else:
              savecard = Supplier()
              savecard.supplier_name = suname
              savecard.supplier_address = sadd
              savecard.supplier_contact = smo
              savecard.supplier_mail = smail  
              savecard.supplier_comp_name = cname
              savecard.supplier_comp_address = cadd
              savecard.supplier_comp_mail = cmail 
              savecard.supplier_comp_bank = bank
              savecard.supplier_comp_acc = ano                          
              savecard.supplier_user = sname
              savecard.supplier_password = spass
              savecard.save()               
              return render(request, 'admin/supplier.html', data) 

def a_index(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    return render(request, 'admin/a_index.html')

def add_prod(request): 
    data = {}
    data['ad_user'] = request.session.get('a_user')
    # return render(request, 'admin/add_product.html', data)
    if request.method == "GET": 
            return render(request, 'admin/add_product.html', data)
    else:
         p_name = request.POST.get('pname')
         p_cost = request.POST.get('cost')
         p_cat = request.POST.get('cat')
         p_unit = request.POST.get('unit')
         p_stock = request.POST.get('stock')         
         print(p_cat,p_cost,p_name,p_unit,p_stock)
         cursor1 = conn.cursor()
         cursor1.execute("select * from product where product_name='" + p_name + "'")
         temp1 = cursor1.fetchall()
         rowcount1 = len(temp1)
         print(rowcount1) 
         if rowcount1 == 1:
            data['msg'] = 'product allready exist'
            return render(request, 'admin/add_product.html', data)
         else:
            savecard = Product()
            savecard.product_name = p_name
            savecard.product_price = p_cost
            savecard.product_category = p_cat
            savecard.product_unit = p_unit
            savecard.product_stock = p_stock        
            savecard.save()
            return render(request, 'admin/add_product.html', data)

def ad_prod_all(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')    
    if request.method == "GET":
        showall = Product.objects.all()
        data['result'] = showall
        return render(request, 'admin/product_data.html', data)
    else:
        if 'del' in request.POST:
            info = request.POST.get('en_del')
            cursor1.execute("delete from product where id ='" + info + "'")
            print(info)
            return redirect('product')
        elif 'search' in request.POST:
            name = request.POST.get('prod')
            print(name)
            data['result'] = Product.objects.filter(product_name=name)
            return render(request, 'admin/product_data.html', data)

def up_cus_account(request):
    data = {}
    data['s_user'] = request.session.get('user')
    if request.method == "GET":
        data['result'] = Customer.objects.filter(customer_user=data['s_user'])
        return render(request, 'upd_account.html', data)
    else:
        if 'update' in request.POST:
            c_id = request.POST.get('cid')
            name = request.POST.get('sname')
            addr = request.POST.get('sadd')
            e_mail = request.POST.get('smail')
            mobile = request.POST.get('sno')
            user_name = request.POST.get('user')
            pass_word = request.POST.get('s_pass')
            print(c_id,name,addr,e_mail,mobile,user_name,pass_word)
            # Updating the records
            sql = "UPDATE customer SET customer_name = '" + name + "',customer_address ='" + addr + "',customer_contact ='" + mobile + "',customer_mail ='" + e_mail + "',customer_user ='" + user_name + "',customer_password ='" + pass_word + "' where id='" + c_id + "'"
            cursor1.execute(sql)
            print("Table updated...... ")
            return redirect("c_profile")
        
def stock_add(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    data['result1'] = Product.objects.all()
    data['result'] = Product.objects.filter(product_stock__lt = 5)
    if request.method == "GET":
        return render(request, 'admin/stock.html', data)
    else:
        if 'search' in request.POST:
            name = request.POST.get('prod')
            print(name)
            data['result2'] = Product.objects.filter(product_name=name)
            return render(request, 'admin/stock.html', data) 
        else:
            c_id = request.POST.get('cid')
            name = request.POST.get('sname')
            cost = request.POST.get('cost')
            unit = request.POST.get('unit')
            p_qty = request.POST.get('qty')
            qty = request.POST.get('p_qty')            
            t_date = datetime.today().strftime('%Y-%m-%d') 
            print(c_id,name,cost,unit,p_qty,cost,t_date,qty)
            a = int(qty) 
            b = int(p_qty)
            c = a + b
            print(c)
            f_stock = str(c)
            savecard = Stock()
            savecard.product_id = c_id
            savecard.product_name = name
            savecard.product_price = cost
            savecard.product_unit = unit
            savecard.add_stock = p_qty
            savecard.Stock_date = t_date            
            savecard.save()
            sql = "UPDATE product SET product_stock ='" + f_stock + "' where id='" + c_id + "'"
            cursor1.execute(sql)               
            return render(request, 'admin/stock.html', data)
     
def receipt(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    template = get_template('admin/user_receipt.html')
    context = {
                "invoice_id": "recid",
                "customer_name": "name",
                "address": "uadd",
                "mobile": "umob",
                "mail": "umail",
                "aadhar": "uaadhar",
                "user": "uuser",
                "passw": "rpass"
            }
    html = template.render(context)
    pdf = render_to_pdf('admin/user_receipt.html', context)
    if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "User_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response                   
            return HttpResponse("Not found")

def ad_all_order(request):
    data = {}
    data['ad_user'] = request.session.get('a_user') 
    showall = Order.objects.all() 
    data['result'] = showall 
    if request.method == "GET":
        return render(request, 'admin/all_order.html', data)
    else:
        suname = request.POST.get('name')
        sadd = request.POST.get('add')
        mobile = request.POST.get('no')
        c_user = request.POST.get('user')
        prod = request.POST.get('p_name')
        cost = request.POST.get('price')
        p_qty = request.POST.get('qty')
        add = request.POST.get('total')
        od_date = request.POST.get('o_date')        
        print(suname,sadd,mobile,c_user)
        template = get_template('receipt.html')
        context = {
                "invoice_id": "recid",
                "customer_name": suname,
                "date": od_date,
                "address": sadd,
                "mobile": mobile,
                "user": c_user,
                "product": prod,
                "amount": cost,
                "qty": p_qty,
                "total": add                
            }
        html = template.render(context)
        pdf = render_to_pdf('receipt.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "User_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response                   
            return HttpResponse("Not found")        

def ad_all_feed(request):
    data = {}
    data['ad_user'] = request.session.get('a_user') 
    showall = Feedback.objects.all() 
    data['result'] = showall 
    return render(request, 'admin/all_feed.html', data)        
                 
            
              
