from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catalog.models import Contact, Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)

class ProductCreateView(CreateView):
    model = Product
    fields = ("product_name", "product_description", "product_image", "category", "price")
    success_url = reverse_lazy('catalog:product_list'),

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product_name", "product_description", "product_image", "category", "price")
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

class ProductDetailView(DetailView):
    model = Product
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)



class ContactListView(ListView):
    model = Contact
# def contact_list(request):
#     contacts = Contact.objects.all()
#     context = {'contacts': contacts}
#     if request.method == "POST":
#         name = request.POST.get('name')
#         contact = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя: {name}\nТелефон: {contact}\nСообщение: {message}\n')
#         Contact.objects.create(name=name, phone=contact, message=message)
#     return render(request, 'contact_list.html', context)


class ContactDetailView(DetailView):
    model = Contact
# def contact_detail(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     context = {'contact': contact}
#     return render(request, 'contact_detail.html', context)
