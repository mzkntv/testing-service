from django.db import models


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
