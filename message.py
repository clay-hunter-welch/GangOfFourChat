# Gang of Four project:
# Creational patterns:
#   -Factory
# Structural patterns:
# Behavioral patterns:
# Concurrency patterns:

from users import AbstractUserFactory


# message classes and methods

class Message:
    def process(self):
        pass


class TextMessage(Message):
    def __init__(self, text):
        self.text = text

    def process(self):
        print(f"Processing Text message: {self.text}")


class ImageMessage(Message):
    def __init__(self, image_path):
        self.image_path = image_path

    def process(self):
        print(f"Processing Image message: {self.image_path}")


class AudioMessage(Message):
    def __init__(self, audio_path):
        self.audio_path = audio_path

    def process(self):
        print(f"Processing Audio message: {self.audio_path}")


class DocumentMessage(Message):
    def __init__(self, document_path):
        self.document_path = document_path

    def process(self):
        print(f"Processing Document message: {self.document_path}")


class CommandMessage(Message):
    def __init__(self, command):
        self.command = command

    def process(self):
        print(f"Processing Command message: {self.command}")

        parts = self.command.split(", ")
        action, user_type = parts[0].split(": ")
        details = {part.split(": ")[0]: part.split(": ")[1] for part in parts[1:]}

        if action == "Create User":
            user_builder = AbstractUserFactory.get_user_builder(user_type)
            user = user_builder.set_username(details["Username"]) \
                .set_permissions(details["Permissions"]) \
                .build()


def message_factory(message_type, content):
    match message_type:
        case 'text':
            return TextMessage(content)
        case 'image':
            return ImageMessage(content)
        case 'audio':
            return AudioMessage(content)
        case 'document':
            return DocumentMessage(content)
        case 'command':
            return CommandMessage(content)
        case _:
            raise ValueError("Unknown message type")
