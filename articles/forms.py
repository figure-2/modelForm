from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 기능 1 html 코드를 자동으로 만들어준다. 
    # 그래서 templates의 create.html의 7번째 {{form}}을 이용해서
    # articles의 views의 29번째줄에서 사용한다
    
    class Meta:
        model = Article
        fields = '__all__'
