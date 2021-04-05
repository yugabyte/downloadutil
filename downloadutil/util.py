import logging
import re
import hashlib
import os

from typing import Any


BUFFER_SIZE_BYTES = 128 * 1024

SHA256_CHECKSUM_RE = re.compile(r'^[0-9a-f]{64}$')


def download_file(url: str, dest_path: str) -> str:
    """
    Download a file to the given path and return its SHA256 sum.
    """
    try:
        with open(dest_path, 'wb') as dest_file:
            import urllib.request
            req = urllib.request.Request(url, headers={'user-agent': 'Mozilla'})
            remote_file = urllib.request.urlopen(req)
            try:
                sha256_hash = hashlib.sha256()
                for byte_block in iter(lambda: remote_file.read(BUFFER_SIZE_BYTES), b""):
                    sha256_hash.update(byte_block)
                    dest_file.write(byte_block)
                return sha256_hash.hexdigest()
            finally:
                remote_file.close()
    except:  # noqa
        if os.path.exists(dest_path):
            logging.warn("Deleting the unfinished download: %s", dest_path)
            os.remove(dest_path)
        raise


def validate_sha256sum(checksum_str: str) -> None:
    """
    Validtes the given SHA256 checksum. Raises an exception if it is invalid.
    """
    if not SHA256_CHECKSUM_RE.match(checksum_str):
        raise ValueError(
            "Invalid SHA256 checksum: '%s', expected 64 hex characters" % checksum_str)


def update_hash_with_file(hash: Any, filename: str, block_size: int = BUFFER_SIZE_BYTES) -> str:
    """
    Compute the hash sun of a file by updating the existing hash object.
    """
    # TODO: use a more precise argument type for hash.
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hash.update(block)
    return hash.hexdigest()


def compute_file_sha256(path: str) -> str:
    return update_hash_with_file(hashlib.sha256(), path)
