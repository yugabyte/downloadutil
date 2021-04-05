from downloadutil.download_cache import DownloadCache


class Downloader:
    cache: DownloadCache

    def __init__(self, cache_dir_path: str) -> None:
        self.cache = DownloadCache(cache_dir_path)

    def download_file(self, url: str) -> str:
        """
        Downloads the given URL and returns the downloaded file path.
        """
        pass
