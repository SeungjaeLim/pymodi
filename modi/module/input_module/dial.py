"""Dial module."""

from enum import Enum

from modi.module.input_module.input_module import InputModule


class Dial(InputModule):

    class PropertyType(Enum):
        DEGREE = 2
        TURNSPEED = 3

    def __init__(self, id_, uuid, msg_send_q):
        super().__init__(id_, uuid, msg_send_q)

    def get_degree(self) -> float:
        """Returns the angle of the dial between 0 and 100

        :return: The dial's angle.
        :rtype: float
        """
        return self._get_property(self.PropertyType.DEGREE)

    def get_turnspeed(self) -> float:
        """Returns the turn speed of the dial between 0 and 100

        :return: The dial's turn speed.
        :rtype: float
        """
        return self._get_property(self.PropertyType.TURNSPEED)
