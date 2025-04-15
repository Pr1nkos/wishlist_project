from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wish
from .forms import CustomUserCreationForm
from django.utils import timezone
from django.contrib import messages

@login_required
def wishlist(request):
    editing_wish = request.GET.get('edit')
    if request.method == 'POST' and not editing_wish:
        wish_text = request.POST.get('wish_text')
        if wish_text:
            Wish.objects.create(text=wish_text, user=request.user)
        return redirect('wishlist')
    wishes = Wish.objects.filter(user=request.user)
    return render(request, 
                  'wishes/wishlist.html', 
                  {'wishes': wishes,
                  'editing_wish': int(editing_wish) if editing_wish else None
                  })

@login_required
def delete_wish(request, wish_id):
    if request.method == 'POST':
        wish = Wish.objects.get(id=wish_id, user = request.user)
        wish.delete()
    return redirect('wishlist')

@login_required
def edit_wish(request, wish_id):
    if request.method == 'POST':
        wish = Wish.objects.get(id=wish_id, user = request.user)
        wish_text = request.POST.get('wish_text')
        if wish_text:
            wish.text = wish_text
            wish.edited_at = timezone.now()
            wish.save()
    return redirect('wishlist')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна! Теперь вы можете войти')
            return redirect('login')
        else:
            messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'wishes/register.html', {'form': form})