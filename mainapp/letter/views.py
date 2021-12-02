from django.views.generic import list, detail, base, edit
from .models import ChristmasLetter
from .pdf_generator import PdfGenerator


class HomeView(base.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letters_number'] = ChristmasLetter.objects.all().count()
        return context


class AllLettersView(list.ListView):
    model = ChristmasLetter
    context_object_name = 'letters_list'
    template_name = 'letters.html'
    paginate_by = 8


class LetterCreate(edit.CreateView):
    model = ChristmasLetter
    fields = ['title', 'content', 'signature']


class LetterDetailView(detail.DetailView):
    model = ChristmasLetter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pdf = PdfGenerator(str(self.object),
                           str(self.object.content),
                           str(self.object.signature))
        pdf.create()
        link = pdf.share()

        context['link'] = link
        return context
