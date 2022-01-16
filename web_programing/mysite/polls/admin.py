from django.contrib import admin
from polls.models import Question, Choice

# admin.TabularInline 테이블로 만든다


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    # ChoiceInline 같이 편집할 수 있게 디스플레이
    inlines = [ChoiceInline]
    # 목록에 아래 항목들을 같이 디스틀레이 한다.
    list_display = ('question_text', 'pub_date')
    # 필터 설정
    list_filter = ['pub_date']
    # 서치 바 설정
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
