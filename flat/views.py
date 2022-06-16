from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from . import models,forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .filters import FlatFilter


def home(request):
    return redirect('flats/',request)



@login_required
def search(request):
    flat_list = models.Flat.objects.order_by('-Цена')
    flat_filter = FlatFilter(request.GET,queryset=flat_list)
    return render(request,'index.html',{'filter':flat_filter})



class FlatDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'flat_detail.html'

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get('id')
        return get_object_or_404(models.Flat, id=shows_id)

class FlatAddView(LoginRequiredMixin,generic.CreateView):
    template_name = 'add_flat.html'
    form_class = forms.FlatForm
    queryset = models.Flat.objects.all()
    success_url = '/flats/'

    def form_valid(self, form):
        form.instance.Сотрудники = self.request.user
        return super(FlatAddView, self).form_valid(form=form)


class FlatUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'update_flat.html'
    form_class = forms.FlatForm
    success_url = '/flats/'

    def get_object(self, **kwargs):
        flat_id = self.kwargs.get('id')
        return get_object_or_404(models.Flat,id=flat_id)

    def form_valid(self, form):
        if self.request.user == form.instance.user:
            return super(FlatUpdateView,self).form_valid(form=form)

        else:
            return redirect('/flats/')


class FlatDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'delete_flat.html'
    success_url = '/flats/'

    def get_object(self, **kwargs):
        flat_id = self.kwargs.get('id')
        return get_object_or_404(models.Flat, id=flat_id)





