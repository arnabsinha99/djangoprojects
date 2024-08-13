from django.contrib import admin
from .models import Publisher, Book, Member, Order, Review


class BookAdmin(admin.ModelAdmin):

    # list_display = ('title', 'publisher', 'category')
    fields = [('title', 'category', 'publisher'), ('num_pages', 'price', 'num_reviews')]
    list_display = ('title', 'category', 'price')


class OrderInline(admin.TabularInline):
    model = Order


class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'status', 'city')
    inlines = [OrderInline]


class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('books',)
        }),
        ('Order Details', {
            'fields': ('member', 'order_type', 'order_date')
        }),
    )

    list_display = ('id', 'member', 'order_type', 'order_date', 'total_items')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'book', 'rating', 'date', 'prnt')
    list_filter = ('rating', 'date')
    search_fields = ('reviewer', 'comments')

    def prnt(self, obj):
        if obj.rating > 3:
            return 'Excellent'
        else:
            return 'Good'

    prnt.short_description = 'Rating of book'  # replaces name in list_display in header on admin change_site


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
