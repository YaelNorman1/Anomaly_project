from abc import ABC, abstractmethod
from typing import List


class DataBaseManager(ABC):
    @abstractmethod
    def get_all_anomalies(self) -> List:
        pass

    @abstractmethod
    def get_user_statistics(self, user_id: int, category: str) -> List:
        pass
