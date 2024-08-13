from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class GroupRequiredMixin(UserPassesTestMixin):
    group_name = None

    def test_func(self):
        if self.group_name:
            return self.request.user.groups.filter(name=self.group_name).exists()
        return False

    def handle_no_permission(self):
        raise PermissionDenied("이 작업을 수행할 권한이 없습니다.")
