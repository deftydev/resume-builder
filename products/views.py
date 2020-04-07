from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

#class based view which does not take login required for configuring
#the user else takes loginrequiredmixing and also we modify settings.py for it and our urls.py
class HomePageView(LoginRequiredMixin,ListView):
    template_name='products/home.html'
    model = Product
    context_object_name='products'

    def get_queryset(self):
        products = super().get_queryset()
        return products.filter(hunter=self.request.user)




class ProductCreateView(LoginRequiredMixin,CreateView):
    model=Product
    template_name='products/create.html'
    fields=['email','address','mobile','career','inter','high','btech','image','work','title1','description1','teamsize1','role1','title2','description2','teamsize2','role2','field','skill1','skill2','skill3','achievement1','achievement2','achievement3','achievement4','achievement5']



    def form_valid(self,form):

        instance=form.save(commit=False)
        instance.hunter=self.request.user
        instance.save()
        subject="Devansh welcomes you"
        message="welcome to clone formed your product go on!"
        from_email=settings.EMAIL_HOST_USER
        to_list=[instance.email]
        send_mail( subject, message, from_email,to_list,fail_silently=True  )
        

        return redirect('home')
#
# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     product=Product()
#     recepient = str(product.email)
#     send_mail( subject, message, email_from,  )
#     return redirect('home')


# in class based like this underneath you have to add form_valid method to save the form and the name of the user who was creating
# and always write pk in class based views.
class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model=Product
    template_name='products/update.html'
    fields=['email','address','mobile','career','inter','high','btech','image','work','title1','description1','teamsize1','role1','title2','description2','teamsize2','role2','field','skill1','skill2','skill3','achievement1','achievement2','achievement3','achievement4','achievement5']
    def form_valid(self,form):
        instance=form.save()
        return redirect('/',instance.pk)



class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model=Product
    template_name='products/delete.html'
    fields=['email','address','mobile','career','inter','high','btech','image','work','title1','description1','teamsize1','role1','title2','description2','teamsize2','role2','field','skill1','skill2','skill3','achievement1','achievement2','achievement3','achievement4','achievement5']
    success_url='/'
    # context_object_name='products'



@login_required(login_url="/accounts/signup")
def detail(request,product_id):
    product=get_object_or_404(Product, pk=product_id)
    return render(request,'products/detail.html',{'product':product})


@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method=="POST":
        product=get_object_or_404(Product , pk=product_id)
        product.votes_total +=1
        product.save()
        return redirect('/products/' + str(product.id))
