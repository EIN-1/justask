from django.contrib import admin
from .models import Category, Question, Reaction
from comments.models import Comment

# Register the category model to be viewed in the admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # show the category name in the list view of categories
    list_display = ( 'name',)

#Register the questions in the admin interface
# Display question list with title, author, category, created_at and updated_at fields
# Search questions by title and content
# Filter questions by category, date it was created and when it was updated
#order the list  by desending the date it was created
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):    
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')    
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('-created_at',)

#Register the Reactions in the admin dashboard
@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'reaction')
    list_filter = ('reaction',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'question', 'content', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
