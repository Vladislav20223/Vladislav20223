from django.contrib.auth.models import User
from django.db import models, transaction


class Book(models.Model):
    title = models.CharField(name='title', max_length=100, unique=True)
    first_page = models.ForeignKey(
        'BookPage', null=True, on_delete=models.SET_NULL,
        related_name='first_name',
    )
    cover_art = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(name='title', max_length=100)
    body = models.TextField(name='body')

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)




    def __str__(self):
        return (
            '{self.from_page.title} ➝ {self.to_page.title} '
            '({self.id})'.format(
                self=self,
            )
        )

    def has_all_needed(self, items):
        return all(i in items for i in self.items.all())



class Item(models.Model):
    name = models.TextField()

    def __str__(self):
        return '{self.name}'.format(self=self)


class DroppedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)


    def __str__(self):
        return '{self.item.name} ({self.book_page.title})'.format(self=self)


class DroppedItemSave(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)



class Note(models.Model):
    text = models.TextField()

    page = models.ForeignKey(
        BookPage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



