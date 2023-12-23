from abc import ABC, abstractmethod



class BaseRepository[DM, MD](ABC):
    def __init__(self, model: MD):
        pass

    @abstractmethod
    def add(self, obj: DM):
        pass

    @abstractmethod
    def get(self) -> DM:
        pass

    @abstractmethod
    def model(self) -> MD:
        pass


class base_repo[R: BaseRepository]:
    def __init__(self, repo: R):
        self.repo = repo
        self.domain = self.repo.get()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.repo.add(self.domain)

