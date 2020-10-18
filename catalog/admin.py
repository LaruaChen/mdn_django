from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


# before
# admin.site.register(Author)

# after
# Define the admin class
# list_display 用表格去顯示()中的欄位
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # 默認情況下，字段是垂直顯示的，但是如果您進一步將它們分組到一個元組中，它們將水平顯示(日期)

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# ------------------------------------------

# before
# admin.site.register(Book)
# admin.site.register(BookInstance)

# after
# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    # extra = 0 是設定將書本的詳細資料只顯示目前是存的資料，不會有空的資料串

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] #利用inline屬性，同時編輯Book物件以及BookInstance物件
    # inlines新增借閱歷史在書本之下

# --------------------------------------------

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
    # 將分成兩區來顯示

# ------------------------------------------
admin.site.register(Genre)
admin.site.register(Language)
# 註冊模型同時註冊資料庫

