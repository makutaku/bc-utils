from abc import ABC, abstractmethod

from contracts import StockContract, FutureContract
from period import Period
from price_series import PriceSeries


class DataStorage(ABC):

    def __init__(self, dry_run: bool):
        self.dry_run = dry_run

    @abstractmethod
    def load_futures(self, contract: FutureContract, period: Period) -> PriceSeries:
        pass

    @abstractmethod
    def load_stock(self, contract: StockContract, period: Period) -> PriceSeries:
        pass

    @abstractmethod
    def persist_futures(self, downloaded_data: PriceSeries, contract: FutureContract, period: Period):
        pass

    @abstractmethod
    def persist_stock(self, df, contract: StockContract, period):
        pass
