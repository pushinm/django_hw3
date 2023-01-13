from django.db import models

# Create your models here.

class Employee(models.Model):

    POSITIONS = [
        ('Оператор', 'Оператор'),
        ('Начальник', 'Начальник'),
        ('Уборщик', 'Уборщик'),
        ('Учитель', 'Учитель'),
        ('Охранник', 'Охранник'),
        ('Бухгалтер', 'Бухгалтер'),
        ('Администартор', 'Администартор'),
    ]

    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    age = models.IntegerField('Возраст', default=18, db_index=True)
    job = models.CharField('Должность', max_length=100, choices=POSITIONS, default=5)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - {self.job}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class Logins(models.Model):
    login = models.CharField('Логин работника', max_length=100, null=False)
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT, null=True)
    def __str__(self) -> str:
        return f'{self.login}'

    class Meta:
        verbose_name = 'Логин'
        verbose_name_plural = 'Логины'