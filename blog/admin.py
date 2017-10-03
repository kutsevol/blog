from django.contrib import admin
from .models import Post, Category, CategoryToPost, Tag, TagToPost


class CategoryInline(admin.TabularInline):
    model = CategoryToPost
    extra = 0


class TagInline(admin.TabularInline):
    model = TagToPost
    extra = 0


class PostMartorAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, TagInline]

    list_display = [field.name for field in Post._meta.fields if field.name not in ('id', 'description', 'text')]
    list_display += ['categories', 'tags']

    list_display_links = ['title', 'slug']
    list_filter = ['category', 'tag']

    search_fields = ['title']

    save_on_top = True
    date_hierarchy = 'created_date'

    fieldsets = [
        (None, {'fields': ['author', 'slug']}),
        ('Body article', {'fields': ['title', 'description', 'text', 'preview_image']}),
        ('Date information', {'fields': ['created_date', 'published_date'],
                              'classes': ['collapse']}),
    ]

    class Meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostMartorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
