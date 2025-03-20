from abc import ABC, abstractmethod

class LatexRecognitionPort(ABC):
    @abstractmethod
    async def recognize_formula(self, image: bytes):
        pass
