from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Меню')
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активно')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('title', )
