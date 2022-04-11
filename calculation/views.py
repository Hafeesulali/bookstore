from django.shortcuts import render
from django.views.generic import View
from calculation.forms import OperationForm


# Create your views here.

# class based view
class AddView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "add.html", {"form": form})

    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = int(n1) + int(n2)
            return render(request, "add.html", {"result": result})
        else:
            return render(request, "add.html", {"form": form})


# function based view
def add(request):
    # print(request.method)
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 + n2
        return render(request, "add.html", {"result": result})
    return render(request, "add.html")


# class based view
class SubView(View):
    def get(self, request):
        forms = OperationForm()
        return render(request, "sub.html", {"form": forms})

    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        forms = OperationForm(request.POST)
        if forms.is_valid():
            n1 = forms.cleaned_data.get("num1")
            n2 = forms.cleaned_data.get("num2")
            result = int(n1) - int(n2)
            return render(request, "sub.html", {"result": result})


# function based views
def sub(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 - n2
        return render(request, "sub.html", {"result": result})
    return render(request, "sub.html")


# class based view
class MulView(View):
    def get(self, request):
        forms = OperationForm()
        return render(request, "multiplication.html", {"form": forms})

    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        forms = OperationForm(request.POST)
        if forms.is_valid():
            n1 = forms.cleaned_data.get("num1")
            n2 = forms.cleaned_data.get("num2")
            result = int(n1) * int(n2)
            return render(request, "multiplication.html", {"result": result})


# function based view
def mul(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 * n2
        return render(request, "multiplication.html", {"result": result})
    return render(request, "multiplication.html")


# class based views
class DivView(View):
    def get(self, request):
        forms = OperationForm()
        return render(request, "divide.html", {"form": forms})

    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        forms = OperationForm(request.POST)
        if forms.is_valid():
            n1 = int(forms.cleaned_data.get("num1"))
            n2 = int(forms.cleaned_data.get("num2"))
            result = n1 / n2
            return render(request, "divide.html", {"result": result})


# function based view
def div(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 / n2
        return render(request, "divide.html", {"result": result})
    return render(request, "divide.html")


def getvowels(request):
    if request.method == "POST":
        word = request.POST.get("word")
        vowels = [char for char in word if char in ["a", "e", "i", "o", "u"]]
        return render(request, "getvow.html", {"result": vowels})

    return render(request, "getvow.html")


def prime(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        prime_numbers = []
        # prime_list = [x for x in range(10, 11) for y in range(2, x) if x % x == 0 and x % 1 == 0 and x % y != 0]
        # prime_numbers = [num for num in range(num1, num2) if num > 0 for i in range(2, num) if num % i != 0]
        for num in range(num1, num2 + 1):
            if num > 0:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    prime_numbers.append(num)
        return render(request, "prime.html", {"prime": prime_numbers})
    return render(request, "prime.html")


def word_count(request):
    if request.method == "POST":
        words = request.POST.get("words")
        word_counts = {}
        for i in words:
            data = i.rstrip("\n").split(" ")
            # print(data)
            for j in data:
                if j not in word_count:
                    word_counts.update({j: 1})
                else:
                    val = word_count[j]
                    val = val + 1
                    word_counts.update({j: val})
        return render(request, "wordcount.html", {"result": word_counts})

    return render(request, "wordcount.html")


class IndexView(View):
    def get(self, request):
        return render(request, "home.html")
