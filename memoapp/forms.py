from django import forms
from .models import Memo

class MemoForm(forms.ModelForm): # ModelForm : DB와 연결된 폼을 만드는 것
    class Meta: # 이름이 Meta인 이유 - 데이터를 설명하는 데이터라서; 어떤 모델, 필드를 폼에서 보여줄 것인지 정보를 담고 있는 부분
        model = Memo # 폼 - Memo 모델과 연결
        fields = ["title", "content"] # 사용자가 수정 가능한 필드
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
        }
        # TextInput & Textarea : HTML의 입력 필드와 텍스트 박스 만드는 것
        # atts는 이해가 안감... 무슨 기능인지 모르겠음 (지피티 사용)


