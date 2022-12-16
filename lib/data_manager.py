import pandas as pd

from typing import Union, Tuple
from binance.client import Client


class DataManager:

    def __init__(self, symbol) -> None:
        self._client = Client("clef_api", "clef_secrete", testnet = False)
        self._symbol: str | None = symbol

        # Gestion dataframe
        self._dataframe: pd.DataFrame | None = None
        self._columns_names: list[str] = ['time', 'open', 'high', 'low', 'close', 'volume']

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe.copy()

    def get_historical_klines(self,
                              start_stop_day: Union[int, Tuple[int, int]] = (1, 31),
                              start_stop_month: Union[str, Tuple[str, str]] = "Jan",
                              start_stop_year: Union[int, Tuple[int, int]] = 2021,
                              kline_interval: str = "1m",
                              format_df: bool = False) -> None:
        """
        On peut retrouver les différents *kline_interval* possible ici :
        'Binance Constants' : https://python-binance.readthedocs.io/en/latest/constants.html
        Il est à chaque fois possible de renseigner, qu'un seul jour, qu'un seul mois ou qu'une
        seule année plutôt que de faire (2021, 2021) par exemple
        .. warning::
            Ne pas mettre le dernier jour du mois si qu'un seul jour est renseigné
        |
        Les klines sont de la forme suivante:
        .. code-block::
            [
              [
                1499040000000,      // Open time
                "0.01634790",       // Open
                "0.80000000",       // High
                "0.01575800",       // Low
                "0.01577100",       // Close
                "148976.11427815",  // Volume
                1499644799999,      // Close time
                "2434.19055334",    // Quote asset volume
                308,                // Number of trades
                "1756.87402397",    // Taker buy base asset volume
                "28.46694368",      // Taker buy quote asset volume
                "17928899.62484339" // Ignore.
              ]
            ]
        :param format_df:
        :param start_stop_day: Jour de début et de fin du dataset
        :type start_stop_day: Union[int, Tuple[int, int]]
        :param start_stop_month: Mois de début et de fin du dataset
        :type start_stop_month: Union[str, Tuple[str, str]]
        :param start_stop_year: Année de début et de fin du dataset
        :type start_stop_year: Union[int, Tuple[int, int]]
        :param kline_interval: Intervale des bougies du dataset
        :type kline_interval: Union[int, Tuple[int, int]]
        """

        ### Definition des donnees temporelles
        start: str = ""
        stop: str = ""

        # Jour
        if type(start_stop_day) is int:
            start += f"{start_stop_day}"
            stop += f"{start_stop_day + 1}"
        else:
            start += f"{start_stop_day[0]}"
            stop += f"{start_stop_day[1]}"

        # Mois
        if type(start_stop_month) is str:
            start += f" {start_stop_month}"
            stop += f" {start_stop_month}"
        else:
            start += f" {start_stop_month[0]}"
            stop += f" {start_stop_month[1]}"

        # Année
        if type(start_stop_year) is int:
            start += f" {start_stop_year}"
            stop += f" {start_stop_year}"
        else:
            start += f" {start_stop_year[0]}"
            stop += f" {start_stop_year[1]}"

        ### Récupération des données
        try:
            klines = self._client.get_historical_klines(self._symbol.upper(),
                                                               kline_interval,
                                                               start,
                                                               stop)
        except AttributeError:
            # Fermeture de la méthode
            print('Erreur lors de la récupération des bougies ')
            return

        ### Construction du dataframe
        self._dataframe = pd.DataFrame(klines).iloc[:, :len(self._columns_names)]
        self._dataframe.columns = self._columns_names
        self._dataframe = self._dataframe.apply(pd.to_numeric)

