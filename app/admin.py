from django.contrib import admin

from .models import Comment, Like, UserCount


admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserCount, 
  list_display=('app_id', 'device_id', 'ip_address', 'created_at'), 
  search_fields = ('device_id', 'app_id'),
  list_filter = ('app_id',)
)