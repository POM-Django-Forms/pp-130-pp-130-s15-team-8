from django.contrib import admin

# Імпортуємо моделі з усіх додатків
from authentication.models import CustomUser
from book.models import Book
from author.models import Author
from order.models import Order

# Користувач
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')

# Книга
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count')
    list_filter = ('id', 'name', 'authors')
    search_fields = ('name',)
    fieldsets = (
        ('Базова інформація', {
            'fields': ('name', 'description', 'count')
        }),
        ('Автори', {
            'fields': ('authors',)
        }),
    )

# Автор
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('name', 'surname', 'patronymic')
    fieldsets = (
        ('ПІБ автора', {
            'fields': ('name', 'surname', 'patronymic')
        }),
        ('Книги', {
            'fields': ('books',)
        }),
    )

# Замовлення
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'end_at', 'plated_end_at', 'is_active')
    list_filter = ('created_at', 'end_at', 'book', 'user', 'is_active')
    fieldsets = (
        ('Незмінна інформація', {
            'fields': ('book', 'user', 'created_at')
        }),
        ('Змінна інформація', {
            'fields': ('plated_end_at', 'end_at', 'is_active')
        }),
    )
