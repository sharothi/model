from import_export import resources

from .models import Quiz, Option

class QuizResource(resources.ModelResource):

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'hints')


class OptionResource(resources.ModelResource):

    class Meta:
        model = Option
        fields = ('id', 'quiz__title', 'title', 'is_correct')

