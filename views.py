from http.client import HTTPResponse
from django.shortcuts import redirect, render
import urllib.request
from django.contrib.messages import constants as messages
from paSSengersformes.models import passengers,orders,ratings
import MySQLdb
from django.contrib import messages



from django.contrib.auth.forms import UserCreationForm


global user
user = ()
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = MySQLdb.connect(db_file)
    except:
        print("error")

    return conn




def login(request):
    print(1)
    if request.method == 'POST':
        a = request.POST['select1']
        username1 = request.POST['id']
        password2 = request.POST['password2']
        conn = create_connection("passengers.sql")
        cur = conn.cursor()
        if a == '2':
            cur.execute("SELECT * FROM passengers")
        if a == '3':
            cur.execute("SELECT * FROM passengers")
        if a == '4':
            cur.execute("SELECT * FROM passengers")
        data = cur.fetchall()
        found = False
        conn.close()
        if a=='2' or a=='3':
            for i in data:
                if username1 in i and str(int(password1)) in i:
                    user = i
                    found = True
        else:
            data2 = (dict(data))
            if data2[str(password1)]==str(username1):
                found=True
        if found and a == '3':
            return render(request, 'Indexes.html', {"fn": user[2], "ln": user[3],"gender":user[6],"age":user[1],"email":user[4],"phone":user[7],"id":5,"country":6})
        elif found and a == '2':
            return render(request, 'Indexes.html', {"fn": user[2], "ln": user[3],"gender":user[6],"age":user[1],"email":user[4],"phone":user[7],"id":5,"country":6})
        elif found and a == '4':
            return redirect('login')
        else:
            messages.error(request, 'Wrong username or password', extra_tags='safe')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')





# @login_required(login_url='login')
# def home_view(request):
#     context = {}
#     return render(request, 'login.html', context)



    
def signup(request):
#     conn = mysql.connector.connect(
#    user='root', password='0549927489Ali!', host='127.0.0.1', database='passengers'
#     )
    
    if request.method == 'POST':
        passport = request.POST['id']
        firstname = request.POST['fn']
        lastname = request.POST['ln']
        email1 = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        age = request.POST['age']
        password11=request.POST['password1']
        password22=request.POST['password2']
        country1 = request.POST['country']
        passengers.objects.create(id=passport,fn=firstname,ln=lastname,email=email1,phone=phone,gender=gender,age=age,password1=password11,password2=password22,country=country1)
        passengers.save()
        '''
        if a == '2':
            cur.execute(
                "INSERT INTO passengers VALUES( " +"'" + passport +"'" + " , " + "'" + firstname + "'" + " , " + "'" + lastname + "'" + " , " + "'" + email1 + "'" + " , " + "'" + phone1 + "'" + " , " +"'" + gender1 +"'" + " , " + "'" + age1 + "'" + " , " +"'" + password11 +"'" + ", " +"'" + password22 +"'" + ", " +"'" + country1 +"'" + " )")
            conn.commit()'''
        
    #conn.close()
    return render(request, 'signup.html')

def Orders(request):
    if request.method == 'POST':
        cold1 = request.POST['cold']
        hot1 = request.POST['hot']
        chair1 = request.POST['chair']
        food1 = request.POST['food']
        other1 = request.POST['other']
        
        orders.objects.create(cold=cold1,hot=hot1,chair=chair1,food=food1,other=other1)
        orders.save()
        
        
    return render(request, 'orders.html')


def Home(request):
    content = {}
    lst = passengers.objects.all()
    content = {'RegisterationForm': lst}
    return render(request, 'home.html', content)

def Homepage(request):
    return render(request,'home.html')

def Index(request):
    return render(request, 'index.html')

def rating(request):
    if request.method == 'POST':
        name1 = request.POST['name']
        worker1 = request.POST['worker']
        rating1 = request.POST['rating']
        
        ratings.objects.create(name=name1,worker=worker1,rating=rating1)
        ratings.save()
        
        
    return render(request, 'rating.html')


def Indexes(request):
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=90&q=title:jones'  
    fileobj = urllib.request.urlopen(url)
    fileobj = fileobj.read()
    print("********************************************************")
    print(fileobj)
    print("********************************************************")
    return render(request, 'Indexes.html',{"data":fileobj})




def forgot(request):
#     conn = mysql.connector.connect(
#    user='root', password='0549927489Ali!', host='127.0.0.1', database='passengers'
#     )
    
    if request.method == 'POST':
        password11=request.POST['password1']
        password22=request.POST['password2']
        passengers.objects.create(password1=password11,password2=password22)
        passengers.save()
        
    return render(request, 'forgot.html')




def show(request):  
    ordered = orders.objects.all()  
    return render(request,"show.html",{'orderd':orders})  
