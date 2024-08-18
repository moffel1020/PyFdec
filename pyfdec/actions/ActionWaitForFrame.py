from dataclasses import dataclass
from typing import ClassVar
from pyfdec.actions.Action import Action
from pyfdec.extended_buffer import ExtendedBuffer


@dataclass
class ActionWaitForFrame(Action):
    action_code: ClassVar[Action.ActionCodes] = Action.ActionCodes.ActionWaitForFrame

    frame: int
    skipCount: int

    @classmethod
    def from_buffer(cls, buffer: ExtendedBuffer):
        frame = buffer.read_ui16()
        skipCount = buffer.read_ui8()
        return cls(frame, skipCount)


Action.register(ActionWaitForFrame)
