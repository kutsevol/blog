from django.contrib import admin

from .models import Post, Category, Tag, TagToPost


class TagInline(admin.TabularInline):
    """
    Horizontal layout for tags on same page with Post.

    model - Which model used

    extra - This controls the number of extra forms the formset will display in
    addition to the initial forms.
    """
    model = TagToPost
    extra = 0

# Instead admin.site.register use decorator admin.register that add models on
# the admin site.


@admin.register(Post)
class PostMartorAdmin(admin.ModelAdmin):
    """
    inlines - displayed list of models which will be displayed on the same page
    with PostMartorAdmin

    list_display - which fields displayed on admin page (Posts)

    list_display_links - which fields linked to the inside model

    list_filter - add filter block on admin page (Posts) with the possibility of
    filtration

    search_fields - add search from on admin page (Posts)

    save_on_top - last create post add to the top

    date_hierarchy - above on all posts add filter by date

    fieldsets - The two-tuples are in the format (name, field_options), where
    name is a string representing the title of the fieldset and field_options
    is a dictionary of information about the fieldset, including a list of
    fields to be displayed in it.
    """
    inlines = [TagInline]

    list_display = [field.name for field in Post._meta.fields
                    if field.name not in ('id', 'description', 'text')]
    list_display += ['tags']

    list_display_links = ['title', 'slug']

    list_filter = ['category', 'tag']

    search_fields = ['title']

    readonly_fields = ['created_date', 'updated_date']

    save_on_top = True

    date_hierarchy = 'created_date'

    fieldsets = [
        (None, {'fields': ['author', 'slug', 'status']}),
        ('Body article', {'fields': ['title', 'category', 'description',
                                     'text', 'preview_image']}),
        ('Date information', {'fields': ['created_date', 'updated_date'],
                              'classes': ['collapse']}),
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    prepopulated_fields - slug will be filled based on title
    """
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
