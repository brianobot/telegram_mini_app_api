from users.models import User

class BaseView:
    def get_user(self) -> User | None:
        user_id = self.request.META.get("user_id")
        if not user_id:
            return None
        user, _ = User.objects.get_or_create(id=user_id)
        return user