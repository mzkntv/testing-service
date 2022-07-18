from django.contrib.auth import get_user_model
from django.db import models
from django.utils.datetime_safe import datetime


User = get_user_model()


class TestCase(models.Model):
    title = models.CharField(verbose_name='Наименование тестирования', max_length=255)

    class Meta:
        verbose_name = 'тестирование'
        verbose_name_plural = 'тестирования'

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса')
    test_case = models.ForeignKey(verbose_name='Тестирование', to=TestCase, on_delete=models.SET_NULL, null=True)
    next_question = models.ForeignKey(
        verbose_name='Следующий вопрос',
        to='self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_first = models.BooleanField(verbose_name='Вопрос является первым', default=False)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.TextField(verbose_name='Текст ответа')
    is_correct = models.BooleanField(verbose_name='Ответ является правильным')
    question = models.ForeignKey(verbose_name='Вопрос', to=Question, on_delete=models.CASCADE, related_name='choices')

    class Meta:
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответа'

    def __str__(self):
        return self.text


class ProcessingTestCase(models.Model):
    IN_PROGRESS_STATE_CHOICE = 'in_progress'
    COMPLETED_STATE_CHOICE = 'completed'
    STATE_CHOICES = (
        (IN_PROGRESS_STATE_CHOICE, 'В процессе'),
        (COMPLETED_STATE_CHOICE, 'Завершено'),
    )
    status = models.CharField(
        verbose_name='Статус',
        choices=STATE_CHOICES,
        default=IN_PROGRESS_STATE_CHOICE,
        max_length=255,
    )
    started_at = models.DateTimeField(verbose_name='Дата начала прохождения теста', default=datetime.now)
    test_case = models.ForeignKey(verbose_name='Шаблон тестирования', to=TestCase, on_delete=models.CASCADE)
    current_question = models.ForeignKey(
        verbose_name='Текущий вопрос',
        to=Question,
        on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(verbose_name='Тестируемый', to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'прохождение тестирования'
        verbose_name_plural = 'прохождения тестирования'

    def __str__(self):
        return f'{self.test_case.title} - {self.started_at}'


class Answer(models.Model):
    question = models.ForeignKey(verbose_name='Вопрос', to=Question, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(verbose_name='Выбранные ответы', to=Choice)
    processing_test_case = models.ForeignKey(
        verbose_name='Тестирование',
        to=ProcessingTestCase,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return f'{self.processing_test_case}'
