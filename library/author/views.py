from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import AuthorForm


def is_admin(user):
    return user.is_librarian


@login_required
@user_passes_test(is_admin)
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


@login_required
@user_passes_test(is_admin)
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
        messages.error(request, 'Ім’я автора не може бути порожнім')
    return render(request, 'author_create.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if not author.books.exists():
        author.delete()
        messages.success(request, 'Автор видалений')
    return redirect('author_list')
