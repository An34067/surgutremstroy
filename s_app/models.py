from django.db import models

class Department(models.Model):
    name = models.CharField('Название', max_length=200)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Вышестоящее подразделение')
    description = models.TextField('Описание', blank=True)
    address = models.CharField('Адрес', max_length=400, blank=True)
    phone = models.CharField('Телефон', max_length=30, blank=True)
    email = models.EmailField('Email', blank=True)
    working_hours = models.CharField('Режим работы', max_length=200, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=200)
    position = models.CharField('Должность', max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Место работы')
    photo = models.ImageField('Фото', upload_to='employees/', blank=True, null=True)
    phone = models.CharField('Телефон', max_length=30, blank=True)
    cabinet = models.CharField('Кабинет', max_length=20, blank=True)
    email = models.EmailField('Email', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['order', 'full_name']

    def __str__(self):
        return self.full_name

class WorkType(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Подразделение')
    staff = models.PositiveIntegerField('Кол-во сотрудников', default=0)
    photo = models.ImageField('Фото', upload_to='worktypes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Вид работ'
        verbose_name_plural = 'Виды работ'
        ordering = ['name']

    def __str__(self):
        return self.name

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('working', 'Работает'),
        ('repair', 'На ремонте'),
        ('decommissioned', 'Списано'),
    ]

    title = models.CharField('Название', max_length=300)
    description = models.TextField('Описание', blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Подразделение')
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ответственный')
    purchase_date = models.DateField('Дата приобретения', blank=True, null=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='working')
    location = models.CharField('Местонахождение', max_length=300, blank=True)

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['title']

    def __str__(self):
        return self.title

class Photo(models.Model):
    equipment = models.ForeignKey(
        Equipment, 
        on_delete=models.CASCADE, 
        related_name='photos',
        verbose_name='Оборудование'
    )
    photo = models.ImageField('Фото', upload_to='equipment/')
    caption = models.CharField('Подпись', max_length=300, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['order']

    def __str__(self):
        return f'Фото — {self.equipment.title}'

class News(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    content = models.TextField('Содержание')
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор')
    published_at = models.DateField('Дата публикации', auto_now_add=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    cover = models.ImageField('Обложка', upload_to='news/', blank=True, null=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
    
class Vacancy(models.Model):
    title = models.CharField('Должность', max_length=300)
    requirements = models.TextField('Требования', blank=True)
    slots = models.PositiveIntegerField('Вакантных мест', default=0)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['title']

    def __str__(self):
        return self.title