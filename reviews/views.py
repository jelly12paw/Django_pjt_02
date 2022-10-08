from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def main(request):
    return render(request, 'reviews/main.html')

def index(request):
    contents = Review.objects.order_by('-pk')

    context= {
        'contents' : contents,
    }

    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()

    context = {
        'review_form' : review_form,
    }

    return render(request, 'reviews/create.html', context)

def detail(request, pk):

    content = Review.objects.get(pk=pk)

    context = {
        'content' : content,
    }

    return render(request, 'reviews/detail.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect('/index')

def update(request, pk):

    content = Review.objects.get(pk=pk)
    
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=content)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm(instance=content)

    context = {
        'review_form' : review_form,
    }

    return render(request, 'reviews/update.html', context)