# Gang of Four project:
# Creational patterns:
#   -Abstract factory
#   -Builder
#   -Prototype
# Structural patterns:
# Behavioral patterns:
# Concurrency patterns:

class User:
    def __init__(self):
        self.name = None
        # add other basic user properties
        self.title = None
        self.permissions = 'basic'
        self.about = None
        self.image = None


class UserBuilder:
    def __init__(self):
        self.user = User()

    def set_name(self, name):
        self.user.name = name
        return self

    def set_title(selfself, title):
        self.user.title = title
        return self

    # add other setter methods here

    def build(self):
        return self.user


class RegularUserBuilder(UserBuilder):
    def set_basic_permissions(self):
        # set permissions here
        return self


class ModeratorUserBuilder(UserBuilder):
    def set_moderation_permissions(self):
        # set permissions here
        return self


class AdministratorUserBuilder(UserBuilder):
    def set_administrative_permissions(self):
        # set permissions
        return self

    def set_administrative_access(self):
        # set action access
        return self


class AbstractUserFactory:
    @staticmethod
    def get_user_builder(user_type):
        match user_type:
            case 'RegularUser':
                return RegularUserBuilder()
            case 'Moderator':
                return ModeratorUserBuilder()
            case 'AdministratorUser':
                return AdministratorUserBuilder()
            # Add more conditions for other user types
            case _:
                raise ValueError(f"Unknown user type: {user_type}")
