from django.shortcuts import render
from .models import Post, Prescriptions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, edit, TemplateView
from .forms import PostForm, PresForm

# Create your views here.
class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class Clothes(TemplateView):
	template_name = 'clothes.html'

class Yt(TemplateView):
	template_name = 'yt.html'

class Insurance(TemplateView):
	template_name = 'insurance.html'

class Govt(TemplateView):
	template_name = 'govt.html'

class Vaccine(TemplateView):
	template_name = 'vaccine.html'

class Babysitter(TemplateView):
	template_name = 'babysitter.html'

class Health(TemplateView):
	template_name = 'nutrition.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class AddPres(CreateView):
	model = Post
	form_class = PresForm
	template_name = 'add_pres.html'

class Feed(ListView):
	model = Post
	template_name = 'my_feed.html'
	ordering = ['-post_date']

class Pres(ListView):
	model = Prescriptions
	template_name = 'my_prescriptions.html'
	ordering = ['-post_date']