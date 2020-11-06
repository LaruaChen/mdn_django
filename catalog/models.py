from django.db import models
from datetime import date


# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

# 書籍類型模型 (Genre model) 
# 此模型有一個單一的 CharField 字段(name) 被用來描述書籍類別(限制輸入字元長度最多200個，同時也有提示字(help_text))
# 在模型最下方我們宣告一個 __str__() 方法來簡單回傳被特定一筆紀錄定義的書籍類別名稱。


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self): # 回傳欄位名稱，用來記錄在django後台
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
# 語言模型


from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    # on_delete 當"中文"的這筆資料被刪除，跟"中文"有關聯的資料都會被刪除。舉例A book的語言是中文，因為"中文"欄位被刪除，所以A book的語言欄位就變成空值

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

# 書本模型 (Book model)
# 作者(author)被宣告為外鍵(ForeignKey)，因此每本書只會有一名作者
# on_delete=models.SET_NULL 表示如果某筆作者紀錄被刪除的話，與該作者相關連的欄位都會被設成 Null，允許有null值
# 這個模型定義了 __str__() ，使用書本的 title 字段來回傳一筆 Book 的紀錄
# get_absolute_url() ，根據id回傳url，之後reverse()會根據參數去urls.py找相同的參數名稱

import uuid # Required for unique book instances
# from datetime import date

from django.contrib.auth.models import User  # Required to assign User as a borrower
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)
        permissions = (("can_view_all_borrowed_books","can_edit_all_borrowed_books"),)
        # 定義一個權限，可標記用戶標記已退回一本書 設定管理者權限
        # https://dotblogs.com.tw/kevinya/2018/07/16/093635

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)

# 書本詳情模型 (BookInstance model)
# id 唯一值，全域的唯一值
# book 不會有相同的書本
# imprint 版本說明
# due_back 預計歸還日期， blank屬性是true時欄位不能是空值
# LOAN_STATUS 借閱狀況
# status 狀態

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

# 作者模型(Author model)