from django.shortcuts import render,redirect
from .forms import LoginForm



def index(request):
	return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลลง MySQL
            return redirect('success_page')  # เมื่อบันทึกเสร็จแล้วไปที่หน้าถัดไป
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# ฟังก์ชันสำหรับหน้า Movie Detail
def movie_detail(request, id):
    context = {'movie_id': id}
    return render(request, 'movie_detail.html', context)

# ฟังก์ชันสำหรับหน้า Coming Soon
def coming_soon_detail(request, id):
    context = {'coming_soon_id': id}
    return render(request, 'coming_soon_detail.html', context)

# ฟังก์ชันสำหรับหน้า Celebrity Detail
def celebrity_detail(request, id):
    context = {'celebrity_id': id}
    return render(request, 'celebrity_detail.html', context)

# ฟังก์ชันสำหรับหน้า News Detail
def news_detail(request, id):
    context = {'news_id': id}
    return render(request, 'news_detail.html', context)

