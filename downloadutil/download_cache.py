class DownloadCache:
    cache_dir_path: str

    """
    A directory containing downloaded files and their checksum files.
    """
    def __init__(self, cache_dir_path: str) -> None:
        self.cache_dir_path = cache_dir_path
