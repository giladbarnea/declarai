from typing import List

from pydantic.main import BaseModel

from .base import BaseChatMessageHistory
from declarai.operators.base.types import Message


class InMemoryMessageHistory(BaseChatMessageHistory, BaseModel):
    """
    This memory implementation stores all messages in memory in a list.
    """
    messages: List[Message] = []

    @property
    def history(self) -> List[Message]:
        """
        Returns the list of messages stored in memory.
        :return: List of messages
        """
        return self.messages

    def add_message(self, message: Message) -> None:
        """
        Adds a message to the list of messages stored in memory.
        :param message: the message content and role
        """
        self.messages.append(message)

    def clear(self) -> None:
        self.messages = []
