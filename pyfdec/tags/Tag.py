from abc import ABC, abstractmethod
from enum import Enum
from typing import ClassVar

from pyfdec.extended_buffer import ExtendedBuffer


class Tag(ABC):
    class TagTypes(Enum):
        End = 0
        ShowFrame = 1
        DefineShape = 2
        PlaceObject = 4
        RemoveObject = 5
        DefineBits = 6
        DefineButton = 7
        JPEGTables = 8
        SetBackgroundColor = 9
        DefineFont = 10
        DefineText = 11
        DoAction = 12
        DefineFontInfo = 13
        DefineSound = 14
        StartSound = 15
        DefineButtonSound = 17
        SoundStreamHead = 18
        SoundStreamBlock = 19
        DefineBitsLossless = 20
        DefineBitsJPEG2 = 21
        DefineShape2 = 22
        DefineButtonCxform = 23
        Protect = 24
        PlaceObject2 = 26
        RemoveObject2 = 28
        DefineShape3 = 32
        DefineText2 = 33
        DefineButton2 = 34
        DefineBitsJPEG3 = 35
        DefineBitsLossless2 = 36
        DefineEditText = 37
        DefineSprite = 39
        FrameLabel = 43
        SoundStreamHead2 = 45
        DefineMorphShape = 46
        DefineFont2 = 48
        ExportAssets = 56
        ImportAssets = 57
        EnableDebugger = 58
        DoInitAction = 59
        DefineVideoStream = 60
        VideoFrame = 61
        DefineFontInfo2 = 62
        EnableDebugger2 = 64
        ScriptLimits = 65
        SetTabIndex = 66
        FileAttributes = 69
        PlaceObject3 = 70
        ImportAssets2 = 71
        DefineFontAlignZones = 73
        CSMTextSettings = 74
        DefineFont3 = 75
        SymbolClass = 76
        Metadata = 77
        DefineScalingGrid = 78
        DoABC = 82
        DefineShape4 = 83
        DefineMorphShape2 = 84
        DefineSceneAndFrameLabelData = 86
        DefineBinaryData = 87
        DefineFontName = 88
        StartSound2 = 89
        DefineBitsJPEG4 = 90
        DefineFont4 = 91

    #NOTE: This is a class variable, so it is shared between all instances of this class
    # this variable is ingored by the dataclass module
    tag_type: ClassVar[TagTypes]

    @classmethod
    @abstractmethod
    def from_buffer(cls, buffer: ExtendedBuffer):
        pass
