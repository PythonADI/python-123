from django.contrib import admin
from core.models import Post, Author

admin.site.register([Post, Author])


