from django.contrib.auth.mixins import LoginRequiredMixin
from lots.models import Lot
from django.views.generic import ListView, DetailView, CreateView, TemplateView


class LotListView(ListView):
    model = Lot
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.filter(status=Lot.PLACED)


class LotCreateView(LoginRequiredMixin, CreateView):
    # form_class = CourseCreateForm
    model = Lot
    template_name = 'create.html'
    success_url = '/'
    fields = ['title', 'price']

    def form_valid(self, form):
        lot = form.save(commit=False)
        lot.created_by = self.request.user
        print(self.request.user)
        lot.save()
        return super(LotCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LotCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Add lot'})
        return context


class UserProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'


class LotDetailView(LoginRequiredMixin, DetailView):
    model = Lot
    template_name = 'lot_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = Lot.objects.filter(id=kwargs['pk'], created_by=request.user).update(status=Lot.FINISHED)
        context = super(LotDetailView, self).get_context_data(**kwargs)
        return self.render_to_response(context=context)
