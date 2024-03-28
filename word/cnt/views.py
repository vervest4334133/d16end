from django.urls import reverse_lazy
from django.views.generic import CreateView

from word.cnt.forms import WordForm
from word.cnt.models import Word


class PostList(CreateView):
    form_class = WordForm
    model = Word
    template_name = 'index.html'

    def form_valid(self, form):
        word = form.save(commit=False)
        word.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')

    def main(self):
        if action == 'load':
            return get_file()

        elif action == 'wordcount':
            return get_word('червяк')

        elif action == 'clear-memory':
            return clear_count()