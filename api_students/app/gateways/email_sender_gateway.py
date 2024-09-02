from abc import ABC, abstractmethod


class EmailSenderGateway(ABC):
    @staticmethod
    @abstractmethod
    def send_email(name, email, password):
        pass