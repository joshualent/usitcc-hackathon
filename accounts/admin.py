from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "age",
        "city",
        "state",
        "is_staff",
        "is_active",
    )
    search_fields = ("username", "email", "city", "state")
    ordering = ("username",)

    # Ensure only valid fields are used
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "age", "city", "state")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "age",
                    "city",
                    "state",
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        # Call the parent save method
        super().save_model(request, obj, form, change)

        # Ensure that the user has a profile after being saved
        if not hasattr(obj, 'profile'):  # Check if the profile already exists
            Profile.objects.create(user=obj)

