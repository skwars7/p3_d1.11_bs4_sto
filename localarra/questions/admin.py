from django.contrib import admin
from .models import Posts, CloseReasonTypes, PostTypes, PostTags, Tags, VoteTypes, Votes 

admin.site.register(CloseReasonTypes)
admin.site.register(PostTypes)
admin.site.register(Posts)
admin.site.register(Tags)
admin.site.register(PostTags)
admin.site.register(VoteTypes)
admin.site.register(Votes)