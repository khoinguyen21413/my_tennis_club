from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import LoginForm

def accounts(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(">>>>>> form.is_valid()")
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            print(">>>>>> username_input:", username_input)
            print(">>>>>> password_input", password_input)

            try:
                user = User.objects.get(username=username_input)
                if user.password == password_input:                                         
                    print(">>>>> Login thanh cong")
                    return redirect('home')
                else:
                    print(">>>>> Nhap sai password") 
            except User.DoesNotExist:
                print("User khong ton tai")


            # Get record voi username trong db
            # userdb = User.objects.filter(username=username)

            # # Kiem tra xem usernam co ton tai trong database
            # if not userdb.exists():
            #     print('username khong ton tai')
            #     messages.error(request, 'User does not exist')
            #     return render(request, 'login.html', {'form': form})
            
            # print('Username ton tai trong database')
            # if userdb.
            # # Kiem tra trong tin dang nhap 

            # if user:
            #     print(">>>>>>>Login thanh cong")
            #     login(request, user)
            #     return redirect('home')  # Đổi 'home' thành tên URL của trang đích
            # else:
            #     print(">>>>>>>Login that bai")
            #     form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
