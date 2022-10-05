from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()


class EmailOrUsernameModelBackend(object):
    """
    This is a ModelBacked that allows authentication
    with username or an email.
    """

    def authenticate(
            self, request, username=None, password=None, **kwargs
    ):
        if username is None and "email" in kwargs:
            username = kwargs["email"]

        if "@" in username:
            kwargs = {"email": username}
        else:
            kwargs = {"username": username}

        try:
            user = User.objects.get(**kwargs)

            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id: int):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None

    def get_user_permissions(self, user_obj):
        return user_obj.user_permissions.all()

    def get_group_permissions(self, user_obj):
        user_groups_field = get_user_model()._meta.get_field('groups')
        user_groups_query = 'group__%s' % user_groups_field.related_query_name()
        return Permission.objects.filter(**{user_groups_query: user_obj})

    def get_all_permissions(self, user_obj, obj=None):
        return {
            *self.get_user_permissions(user_obj),
            *self.get_group_permissions(user_obj),
        }

    def has_perm(self, user_obj, perm, obj=None):
        return any([perm == permission.codename for permission in self.get_all_permissions(user_obj, obj=obj)])
