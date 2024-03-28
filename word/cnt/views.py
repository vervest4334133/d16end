from django.contrib.admin import action
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

    def get_file(self):
        f = open('filename.txt', 'r', encoding='utf8')
        text = f.readlines()
        f.close()
        text = text.replace(" ", )
        text = text.replace("\n", )
        text = text.replace("\n", " ")
        return text

    def get_word(self):
        self.process.get('a')
        for word, cnt in self.process().items():
            return f"Слово {word} встречается {cnt} раз"

    def process(text):
        wordcount = {}
        for word in text:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
        return wordcount

    def clear_count(self):
        self.process().clear()
        return self.process()

    def main(self):
        if action == 'load':
            return self.get_file()

        elif action == 'wordcount':
            return self.get_word('червяк')

        elif action == 'clear-memory':
            return self.clear_count()
