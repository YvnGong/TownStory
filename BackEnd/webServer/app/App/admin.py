from django.contrib import admin
from .models import City, Story, Like
# Register your models here.
admin.site.register(City)


# custom story form
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'city', 'id')
admin.site.register(Story, StoryAdmin)

# custom like form
class LikeAdmin(admin.ModelAdmin):
    list_display = ('story_id', 'liked_user')
admin.site.register(Like, LikeAdmin)