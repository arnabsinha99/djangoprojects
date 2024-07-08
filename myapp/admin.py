from django.contrib import admin
from .models import Publisher, Book, Member, Order, Review


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'category')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'status', 'city')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('member', 'order_date','total_items')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'book', 'rating', 'date')
    list_filter = ('rating', 'date')
    search_fields = ('reviewer', 'comments')

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)