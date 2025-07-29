from pathlib import Path
import pymupdf
from caching import persistent_cache

@persistent_cache
def extract_text(file: Path) -> str:
    with pymupdf.open(file) as doc:
        return chr(12).join([page.get_text() for page in doc])
