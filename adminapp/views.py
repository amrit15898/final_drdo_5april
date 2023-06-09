from django.shortcuts import render,redirect
from home.models import * 
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from home.models import postions
from django.contrib.auth.decorators import login_required
# Create your views here.\
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
import random 


@login_required
def admin_panel(request):
    usercount = 0
    appcount = 0
    departmentcount = 0
    departments = {}
    users  = {}
    
    if request.user.is_staff == True:
        try:
            users = User.objects.exclude(is_staff = True)
            usercount = User.objects.all().exclude(is_staff = True).count()
            departmentcount = Department.objects.all().count()
            appcount = Appointment.objects.all().count()   
            departments = Department.objects.all()   
            print() 
        except Exception as e:
            messages.error(request, "Something went wrong.")       
        # try:
            
        # except Exception as e:
        #     print(e)
            
        # paginator = Paginator(users, 4)
        # page_no = request.GET.get("page")
        # userDataFinal = paginator.get_page(page_no)
        
        context = {}
        context["users"] = users
        context["departments"] = departments
        context["usercount"] = usercount
        context["departmentcount"] = departmentcount
        context["appcount"] = appcount
        return render(request, "mainpage.html",context)
    # return render(request, "notfound.html")
    else:
        return redirect("/")


@login_required 
def delete_user(request,id):
    if request.user.is_staff == True:
        try: 
            user1 = User.objects.get(id=id) 
            user1.delete()
            return redirect("/adminpanel/suhrs")     
        except User.DoesNotExist:
            messages.warning(request, "Something went wrong, user not deleted.")
            return redirect("/adminpanel/suhrs")
    return redirect('/')

            
    
@login_required
def update_user(request,id):
    if request.user.is_staff == True:
        context={}
        try:
            gh_dh_user =User.objects.filter(position= "GH/DH")
            tech_dir_users = User.objects.filter(position = "Tech Director")

            user1 = User.objects.get(id=id)
            context["gh_dh_users"] =gh_dh_user
            context["tech_dir_users"]= tech_dir_users
            context = {"user": user1}      
            context["gh_dh_users"] =gh_dh_user
            context["tech_dir_users"]= tech_dir_users
            if request.method =="POST":
                name = request.POST.get("name")
                employee_id = request.POST.get("employee_id")
                position = request.POST.get("position")
                file = request.FILES.get("img")
                get_dh_id= request.POST.get("gh_dh")
                designation = request.POST.get("designation")
                get_tech_dir_id =request.POST.get("tech_dir")
                gh_dh = User.objects.filter(id=get_dh_id).first()
                print(gh_dh)
                tech_dir = User.objects.filter(id=get_tech_dir_id).first()
                # password = request.POST.get("password")
                user1.name = name 
                user1.position = position
                user1.employee_id = employee_id
                user1.image = file 
                user1.gd_dh_user = gh_dh
                user1.tech_dir_user= tech_dir
                user1.designation= designation
                # user1.set_password(password) 
                user1.save()
                # user1.save(using="new")
                return redirect("/adminpanel")
        except Exception as e:
            print(e)
            messages.info(request, "Something went wrong.")
            return HttpResponseRedirect(request.path_info)
        return render(request, "updateuser.html",context)
    
    return redirect("/")



@login_required
def add_user(request):
    if request.user.is_staff == True:
        departments = Department.objects.all()
        gh_dh_user =User.objects.filter(position= "GH/DH")
        tech_dir_users = User.objects.filter(position = "Tech Director")
        oic_user = User.objects.filter(position="oic")
        context = {}
        context["ld_users"] = oic_user
        context["gh_dh_users"] =gh_dh_user
        context["tech_dir_users"]= tech_dir_users

        if request.method=="POST":
            char = list("abcdefghijklmonpqrstuvwxyz")
            length = 9
            rpassword = ""
            for i in range(length):
                rpassword+=random.choice(char)
            print("password is"+rpassword)
            position = request.POST.get("position")
            pis = request.POST.get("pis")
            name = request.POST.get("name")
            
            password = request.POST.get("password")
            employee_id = request.POST.get("userid")
            adhaar_no = request.POST.get("adhaar_no")
            file = request.FILES.get("img")
            designation = request.POST.get("designation")
            get_dh_id= request.POST.get("gh_dh")
            get_tech_dir_id =request.POST.get("tech_dir")
            print(get_dh_id, get_tech_dir_id)
            gh_dh = []
            tech_dir = []
            try:
                gh_dh = User.objects.filter(id=get_dh_id).first()
                tech_dir = User.objects.filter(id=get_tech_dir_id).first()
            except Exception as e:
                print(e)
            obj = User.objects.filter(pis=pis).first()
            if not name:
                messages.info(request, "Employee Name should not be blank.")
                return redirect("/adminpanel/addffadfsfdsf")
            if obj:
                messages.info(request, "User ID already exists. Please enter a different ID.")
                return redirect("/adminpanel/addffadfsfdsf")
            if position == "selectposition":
                messages.info(request, "Please select the position.")
                return redirect("/adminpanel/addffadfsfdsf")
            if not password:
                messages.info(request, "Password required!")
                return redirect("/adminpanel/addffadfsfdsf")
            if not employee_id:
                messages.info(request, "Please enter Employee ID.")
                return redirect("/adminpanel/addffadfsfdsf")

            check_adhaar = User.objects.filter(adhaar_no=adhaar_no).first()
            if check_adhaar:
                messages.info(request,"this adhaar no already register")
                return redirect("/adminpanel/addffadfsfdsf")
            obj = User(position=position, name=name, employee_id=employee_id,pis=pis, image=file, adhaar_no=adhaar_no, designation = designation)

            if gh_dh and tech_dir:
                obj.gh_dh_user = gh_dh
                obj.tech_dir_user = tech_dir

            obj.set_password(password)
            obj.save()
            return redirect("/adminpanel")  
        return render(request, "adduser.html", context)
    return redirect("/")

@login_required
def add_department(request):
    if request.user.is_staff == True:
        if request.method == "POST":
            try:
                name = request.POST.get("name")
                obj = Department.objects.filter(name=name)
                if obj:
                    messages.warning(request,"Department already exists.")
                    return redirect("/")
                obj = Department(name=name)
                obj.save()  
                return redirect("/adminpanel/sfdddaf")        
                # obj.save(using = "new")
            except Exception as e:
                messages.warning(request, "Something went wrong.", + str(e))   
                return redirect("/adminpanel")

        return render(request, "adddepartment.html")
    return redirect("/")
@login_required
def update_department(request, id):
    if request.user.is_staff == True:
        try:
            dep1 = Department.objects.using("default").get(id=id)
            # dep2 = Department.objects.using("new").get(id=id)
        except Exception as e:
            messages.warning(request, "Something went wrong.")
        
        if request.method=="POST":
            name = request.POST.get("name")
            dep1.name= name
            # dep2.name = name 
            try:
                dep1.save()      
                # dep2.save(using="new")
                return redirect("/adminpanel/sfdddaf")
            except Exception as e:
                pass

        context = {
            "dep": dep1
        }
        return render(request, "updatedep.html", context)

    return redirect("/")

def login_front_page(request):
    if request.method=="POST":
        pis = request.POST.get("pis")
        print(pis)
        password = request.POST.get("password")
        if pis == "":
            messages.warning(request, "Please enter User ID.") 
        if password == "":
            messages.warning(request, "Please enter Password.")
        obj = User.objects.filter(pis=pis).first()
        if not obj:
            messages.info(request, "This employee ID does not exist.")
            return redirect("/")    
        user = authenticate(request, pis=pis, password = password)
        if user is not None:
            try:
                login(request, user)
                print("login hoya")
                print(postions[3][1])
                if request.user.is_superuser == True:
                    return redirect("/adminpanel")      
                if request.user.position == postions[4][1]:
                    return redirect("/home/postapntent")
                if request.user.position == postions[5][1]:
                    return redirect("/home/sesdfpnel")

                if request.user.position == postions[6][1]:
                    return redirect("/home/oicpanel")
                
                if request.user.department_access == True:
                    return redirect("/home/dpanellsf")
                
                if request.user.position == postions[7][1]:
                    return redirect("/home/hwpanel")
                else:
                    return redirect("/home/shsfsdfow-readfafquest")
                
            except Exception as e:
       
                messages.error(request, "Please check your credentials.")             
        else:
            messages.error(request, "Please enter the correct password.")    
    return render(request, "login.html")



def logout_handle(request):
    logout(request)
    return redirect("/adminpanel/login")


@login_required
def show_full_department(request):
    if request.user.is_staff == True:
        departments = {}
        try:
            departments = Department.objects.all()     
            # departments = Department.objects.using("new")       
        except Exception as e:
            messages.warning(request, "Something went wrong.")
        context = {"departments": departments}
        return render(request, "department.html", context )
    return redirect("/")

@login_required
def delete_department(request,id):
    if request.user.is_staff == True:
        try:
            obj1 = Department.objects.get(id=id)

            obj1.delete()         
            # obj2.delete()
            return HttpResponseRedirect(request.path_info)
        except Exception as e:
            pass
  
        return redirect("/adminpanel/sfdddaf")
    return redirect("/")
        
    

@login_required
def show_users(request):
    if request.user.is_staff == True:
        users = {}
        try:
            users = User.objects.exclude(is_staff=True)
            # users = User.objects.all(using = "new")
        except Exception as e:
            print(e)
        context = {"users": users}
        return render(request, "showalluser.html",context)
    return redirect("/")

@login_required
def show_all_appointments(request):
    if request.user.is_staff == True:
        appointments = {}
        try:       
            appointments = Appointment.objects.all()
            # appointments = Appointment.objects.using("new")
        except Exception as e:
            messages.warning("Something went wrong.")
    
        context = {"objs": appointments}
        return render(request, "showappointment.html",context)
    return redirect("/")
    


def check_template(request):
    return render(request, "mainpage.html")

@login_required
def forgot_message_request(request):
    objs = {}
    try:
        objs = ForgetMessageRequest.objects.filter(action_perform = False) 
    except Exception as e:
        messages.error(request, "Something went wrong.")
    context = {"objs": objs}
    return render(request, "forgotrequest.html", context)

def change_password(request, id):
    try:
        obj = User.objects.get(pis=id)

        if request.method=="POST":
            password = request.POST.get("password")
            print(password)
            request_obj = ForgetMessageRequest.objects.filter(employee_id = obj).first()
            print(request_obj)
            request_obj.action_perform = True
            request_obj.save()
            obj.set_password(password)
            obj.save()
            return redirect("/adminpanel")
    except Exception as e:
            messages.error(request, "Something went wrong.")
            return HttpResponseRedirect(request.path_info)
    return render(request, "changepass.html")



def full_profile(request):
    return render(request, "profile.html")


def change_employee_password(request):
    try:
        if request.method =="POST":
            currentpass = request.POST.get("currentpass")
            newpassword = request.POST.get("newpassword")
            confirmpassword = request.POST.get("confirmpassword")
            obj = authenticate(pis= request.user.pis , password = currentpass)
            if obj:
            
                if newpassword==confirmpassword and newpassword!=currentpass:
                    obj.set_password(newpassword)
                    obj.save()
                    messages.success(request, "Password changed successfully!")
                    return redirect("/")
                else:
                    messages.error(request, "Password does not match!")
            else:
                messages.error(request, "wrong current password")
                return redirect("/adminpanel/changemppas")
    except Exception as e:
        print(e)
    return render(request, "chngemppass.html")

def login_option(request):
    return render(request,"loginway.html")

    
