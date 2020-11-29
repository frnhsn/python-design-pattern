from __future__ import annotation
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractproperty
    def reset(self) -> None:
        pass

    @abstractproperty
    def product(self) -> None:
        pass

    

