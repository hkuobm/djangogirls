#admin:ポストを追加、編集、削除するのに用いる
from django.contrib import admin
from .models import Post

admin.site.register(Post)#モデルをadminページ上で見えるようにする

# Register your models here.
