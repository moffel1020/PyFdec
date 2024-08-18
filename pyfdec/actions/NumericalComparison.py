from dataclasses import dataclass
from typing import ClassVar
from pyfdec.actions.Action import Action
from pyfdec.extended_buffer import ExtendedBuffer


@dataclass
class ActionEquals(Action):
    action_code: ClassVar[Action.ActionCodes] = Action.ActionCodes.ActionEquals


Action.register(ActionEquals)


@dataclass
class ActionLess(Action):
    action_code: ClassVar[Action.ActionCodes] = Action.ActionCodes.ActionLess


Action.register(ActionLess)

@dataclass
class ActionLess2(Action):
    action_code: ClassVar[Action.ActionCodes] = Action.ActionCodes.ActionLess2


Action.register(ActionLess2)
