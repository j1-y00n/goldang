from django import forms

from .models import Post, Review, PostImage, Comment, QuestionAndAnswer


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'restaurant_type',
            'loc',
            # 'image',
        )
    def save(self, commit=True):
        instance = super().save(commit)
        if self.cleaned_data.get('images'):
            for image in self.cleaned_data.get('images'):
                PostImage.objects.create(post=instance, image=image)
        return instance

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)
        widgets = {'image': forms.FileInput(attrs={'multiple': True})}

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = (
            'content',
            'rating',
            'taste_evaluation',
            'image',
        )
        widgets = {
            'content': forms.Textarea(attrs={
                'id': 'ReviewWriting__Main__Text',
                'class': 'ReviewWriting__Main__Text',
                'placeholder': '주문하신 메뉴는 어떠셨나요? 식당의 분위기와 서비스도 궁금해요!',
                'onkeyup': 'TextLength(this)',
                'onkeydown': 'TextLength(this)',
            }),
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = (
            'content',
        )



class QuestionAndAnswerForm(forms.ModelForm):
    
    class Meta:
        model = QuestionAndAnswer
        fields = (
            'title',
            'content',
        )
