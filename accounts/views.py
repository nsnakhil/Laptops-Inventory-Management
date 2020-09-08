from django.shortcuts import render,redirect, get_object_or_404
from .models import Laptops
from .forms import LaptopForm

def home(request):
    return render(request, 'accounts/home.html')

def laptops(request):

    items = Laptops.objects.all()

    print("Laptops Count:", len(items))

    context = { 'items': items, }

    return render(request, 'accounts/laptops.html', context)
    
def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('laptops')
    else:
        form = LaptopForm()
        return render(request, 'accounts/add_laptop.html', { 'form':form })

def update_laptop(request, pk):
    item = get_object_or_404(Laptops, pk = pk)

    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('laptops')
    
    else:
        form = LaptopForm(instance=item)
        return render(request, 'accounts/update_laptop.html', {'form':form})

def delete(request, pk):

    items = Laptops.objects.all()
    
    if request.method == 'POST':
        Laptops.objects.filter(id=pk).delete()
        return redirect('laptops')

    context = {'items': items}

    return render(request, 'accounts/delete.html', context)
