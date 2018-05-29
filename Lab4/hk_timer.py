from datetime import datetime, timedelta


class HkTimer:
    def __init__(self, sec=-1):
        if sec >= 0:
            self.__end = datetime.now() + timedelta(seconds=sec)
        else:
            self.__end = None

    def expired(self) -> bool:
        return self.__end is not None and datetime.now() >= self.__end
