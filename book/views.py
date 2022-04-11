from django.shortcuts import render, redirect
from book.forms import BookForm
from django.views.generic import View
from book.models import Books



class AddBook(View):
    def get(self, request):
        forms = BookForm()
        return render(request, "book_add.html", {"forms": forms})

    def post(self, request):

        forms = BookForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            # qs = Books(
            #     book_name=forms.cleaned_data.get("book_name"),
            #     author=forms.cleaned_data.get("author"),
            #     amount=forms.cleaned_data.get("price"),
            #     copies=forms.cleaned_data.get("copies")
            # )
            # qs.save()
            # return render(request, "book_add.html", {"msg": "book created"})
            return redirect("allbooks")

        else:
            return render(request, "book_add.html", {"forms": forms})


class BookList(View):
    def get(self, request):
        qs = Books.objects.all()
        return render(request, "book_list.html", {"books": qs})


class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        # pass
        # kwargs={'int':3}
        qs = Books.objects.get(id=kwargs.get("id"))
        return render(request, "book_detail.html", {"book": qs})


class BookDeleteView(View):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allbooks")


class ChangeBook(View):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        forms = BookForm(instance=qs)
        return render(request, "book_edit.html", {"form": forms})

    def post(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        forms = BookForm(request.POST,files=request.FILES, instance=qs)
        if forms.is_valid():
            forms.save()
            return redirect("allbooks")
