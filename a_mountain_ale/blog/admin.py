from django.contrib import admin
from blog.models import Post
from django.contrib.auth import get_user_model

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return Post.objects.filter(author=request.user) or qs.none()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = get_user_model().objects.filter(
                username=request.user.username
            )
        return super(PostAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ("author",)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data["author"] = request.user
        request.GET = data
        return super(PostAdmin, self).add_view(
            request, form_url="", extra_context=extra_context
        )

admin.site.register(Post, PostAdmin)