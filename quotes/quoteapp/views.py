from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages


from .models import Quote, Author, Tag
from .forms import AuthorForm, TagForm, QuoteForm


# Create your views here.
# def main(request):
#     return render(request, 'quoteapp/index0.html')
#
# def author(request, author: str):
#     try:
#         author = Author.objects.get(fullname=author)
#     except:
#         author = None
#     context = {"author": author}
#     return render(request, "quoteapp/author.html", context)
#
# def tag(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='quoteapp:main')
#         else:
#             return render(request, 'quoteapp/tag.html', {'form': form})
#
#     return render(request, 'quoteapp/tag.html', {'form': TagForm()})
#
# def quote(request):
#     tags = Tag.objects.all()
#
#     if request.method == 'POST':
#         form = QuoteForm(request.POST)
#         if form.is_valid():
#             new_note = form.save()
#
#             choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
#             for tag in choice_tags.iterator():
#                 new_note.tags.add(tag)
#
#             return redirect(to='quoteapp:main')
#         else:
#             return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': form})
#
#     return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': QuoteForm()})
PER_PAGE = 4
def main(request, page=1):
    #quotes = Quote.objects.all()
    quotes = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'quoteapp/index.html', {"quotes": quotes})
    paginator = Paginator(quotes, per_page=PER_PAGE)

    context = {"quoteapp": paginator.page(page)}
    return render(request, "quoteapp/index.html", context)


def author(request, author: str):
    try:
        author = Author.objects.get(fullname=author)
    except:
        author = None
    context = {"author": author}
    return render(request, "quoteapp/author.html", context)


def tag(request, tag: str, page: int = 1):
    quotes = []
    tag_id = None
    try:
        tag_id = Tag.objects.get(name=tag).id
    except:
        ...
    print(f"{tag=},{tag_id=}")
    if tag_id:
        quotes = Quote.objects.filter(tags=tag_id)

    paginator = Paginator(quotes, per_page=PER_PAGE)
    context = {"quoteapp": paginator.page(page), "tag_query": tag}
    return render(request, "quoteapp/tag.html", context)

    tag = Tag.objects.get(name=tag)
    paginator = Paginator(tag, per_page=PER_PAGE)

    context = {"tag": paginator.page(page)}
    return render(request, "quoteapp/tag.html", context)

@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data["fullname"]
            messages.success(request, f"Author '{fullname}' was created...")
            return render(
                request, "quoteapp/add_author.html", context={"form": AuthorForm()}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, "quoteapp/add_author.html", context={"form": form})

    context = {"form": AuthorForm()}
    return render(request, "quoteapp/add_author.html", context)


@login_required
def add_quote(request, id: int = 0):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.quote = form.cleaned_data['quote']
            new_quote.author = Author.objects.filter(pk=form.cleaned_data['author']).get()
            new_quote.save()

            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist("tags")
            )
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            messages.success(request, "Quote was added....")
        else:
            messages.error(request, "Not added....")
            return render(request, "quoteapp/add_quote.html", {"tags": tags, "authors": authors, "form": form})

    return render(request, "quoteapp/add_quote.html", {"tags": tags, "authors": authors, "form": QuoteForm()})

class AddAuthorView(LoginRequiredMixin, View):
    form_class = AuthorForm
    template_name = "quoteapp/add_author.html"

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data["fullname"]
            messages.success(request, f"Author '{fullname}' was created...")
            return render(
                request, self.template_name, context={"form": self.form_class}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, self.template_name, context={"form": form})
class AddTagView(LoginRequiredMixin, View):
    form_class = TagForm
    template_name = "quoteapp/add_tag.html"

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data["name"]
            messages.success(request, f"Tag '{fullname}' was created...")
            return render(
                request, self.template_name, context={"form": self.form_class}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, self.template_name, context={"form": form})




