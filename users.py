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
        self.username = None
        self.password = None
        self.role = None
        # add other basic user properties
        self.email = None
        self.title = None
        self.about = None
        self.image = None
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,  # Consider security implications
            "role": self.role,
            "email": self.email,
            "title": self.title,
            "about": self.about,
            "image": self.image,
        }

class UserBuilder:
    def __init__(self):
        self.user = User()

    def configure(self, username, email, role, password):
        self.set_username(username)
        self.set_email(email)
        self.set_role(role)
        self.set_password(password)
        # self.set_title(title)
        # self.set_about(about)
        # self.set_image(image)
        return self

    def set_username(self, username):
        self.user.username = username
        return self

    def set_role(self, role):
        self.user.role = role
        return self

    def set_password(self, password):
        self.user.password = password
        return self

    def set_email(self, email):
        self.user.email = email
        return self

    def set_title(self, title):
        self.user.title = title
        return self

    def set_about(self, about):
        self.user.about = about
        return self

    def set_image(self, image):
        self.user.image = image
        return self

    def build(self):
        return self.user


class RegularUserBuilder(UserBuilder):
    def set_basic_permissions(self):
        # set permissions here
        return self


class ModeratorUserBuilder(UserBuilder):
    def set_moderator_permissions(self):
        # set permissions here
        return self


class AdministratorUserBuilder(UserBuilder):
    def set_administrator_permissions(self):
        # set permissions
        return self


class AbstractUserFactory:
    @staticmethod
    def get_user_builder(user_type):
        match user_type:
            case 'Regular':
                return RegularUserBuilder()
            case 'Moderator':
                return ModeratorUserBuilder()
            case 'Administrator':
                return AdministratorUserBuilder()
            # Add more conditions for other user types
            case _:
                raise ValueError(f"Unknown user type: {user_type}")
