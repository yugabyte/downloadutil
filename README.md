# downloadutil
A Python module with common utilities for downloading and extracting archives.

Use cases:
- Download an archive from a URL and the expected SHA256 checksum from the same URL with a ".sha256"
  suffix appended. Verify the checksum.
- Download an archive as above and extract it into a target directory, and still keep the archive in
  a special cache directory.
