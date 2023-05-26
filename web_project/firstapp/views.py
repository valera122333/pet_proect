from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from firstapp.models import Pet
from firstapp.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    user = request.user
    pets = Pet.objects.filter(user=user)
    context = {"pets": pets}
    return render(request, "home.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request,f'Аккаунт создан для юзера {username}!'
            )
            return redirect ('home')
            
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render (request,'register.html',context)
    
from .forms import PetForm
@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')   
    else:
        form = PetForm()
    
    return render(request, 'add_pet.html', {'form': form})


@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, "pet_detail.html", {"pet": pet})
 
 
@login_required
def delete_pet(request, pk=None):
    Pet.objects.get(id=pk).delete()
    return redirect('home')



@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, user=request.user)
    
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pet_id=pet_id)
    else:
        form = PetForm(instance=pet)
    
    context = {'form': form, 'pet': pet}
    return render(request, 'edit_pet.html', context)