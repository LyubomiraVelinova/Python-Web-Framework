from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from cbv_demos.web.models import Article


# Create your views here.


def list_articles(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'articles/list.html', context)


# class ArticlesListView(views.View):
#     def post(self):
#         pass
#
#     def get(self):
#         context = {
#             'articles': Article.objects.all(),
#         }
#         return render(self.request, 'articles/list.html', context)


# class ArticlesListView(views.TemplateView):
#     template_name = 'articles/list.html'
#
#     # Static data
#     extra_context = {
#         'articles': Article.objects.all()
#     }
#
#     # Dynamic data
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context


class ArticlesListView(views.ListView):
    template_name = 'articles/list.html'
    model = Article
    paginate_by = 15

    #     Article.objects.filter(name_icontains=search)
    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class ArticleDetailView(views.DetailView):
    model = Article
    template_name = 'articles/details.html'


class RedirectToArticlesView(views.RedirectView):
    url = reverse_lazy('list articles cbv')


class BaseView:
    def get(self, request):
        pass

    def post(self, request):
        pass

    @classmethod
    def as_view(cls):
        self = cls

        def view(request):
            if request.method == 'GET':
                return self.get(request)
            else:
                return self.post(request)

        return view

class ArticleCreateView(views.CreateView):
    model = Article
    template_name = 'articles/create.html'
    fields = '__all__'
    # This is not build in
    disabled_fields = ('title',)
    success_url = reverse_lazy('list articles cbv')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

        return form
