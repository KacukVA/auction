from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from lots.models import Lot
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, TemplateView


# Create your views here.
class LotListView(ListView):
    model = Lot
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.filter(status=Lot.PLACED)


class LotCreateView(CreateView):
    # form_class = CourseCreateForm
    model = Lot
    template_name = 'create.html'
    success_url = '/'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LotCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Add lot'})
        return context


class UserProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'


class LotDetailView(DetailView):
    model = Lot
    template_name = 'lot_detail.html'
