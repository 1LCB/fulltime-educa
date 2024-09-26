class LimitedSizeDictionary(dict):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def __setitem__(self, key, value):
        if len(self) >= self.max_size:
            oldest_key = next(iter(self))
            del self[oldest_key]
        super().__setitem__(key, value)


class CacheManager:
    cache = LimitedSizeDictionary(100)

    @staticmethod
    def get_item(key: str):
        return CacheManager.cache.get(key, None)

    @staticmethod
    def set_item(key: str, value):
        CacheManager.cache[key] = value
