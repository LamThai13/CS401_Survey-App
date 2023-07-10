from django.forms import ModelForm
from .models import Poll,  Rate


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'option_five']


class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['question', 'rate_one', 'rate_two', 'rate_three', 'rate_four', 'rate_five']

