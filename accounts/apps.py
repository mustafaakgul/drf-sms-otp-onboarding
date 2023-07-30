from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

# from django.utils.translation import gettext_lazy as _
# class UserConfig(AppConfig):
#     name = 'user'
#     verbose_name = _('user')