from __future__ import annotations
import hashlib, pickle, os, json, sys
from pathlib import Path
from typing import Callable, Any, Dict, Tuple

CACHE_DIR = Path(os.getenv("XDG_CACHE_HOME", Path.home() / ".cache")) / "lecturenotes"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def _sha256_of_file(p: Path, chunk_size: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

def persistent_cache(
    func: Callable[..., Any],
    *,
    name: str | None = None,
) -> Callable[..., Any]:
    """
    Decorator that memo‑ises *persistently* on disk.
    The cache key is (func‑name, arg‑hashes, kwargs‑hashes).
    For file arguments, the **content hash**, not the Path string, is used.
    """
    func_name = name or func.__name__

    def _serialise(v: Any) -> Tuple[str, bytes]:
        if isinstance(v, Path):
            key = f"file:{_sha256_of_file(v)}"
        else:
            key = f"json:{json.dumps(v, sort_keys=True, default=str)}"
        return key, key.encode()

    def wrapper(*args, **kwargs):
        key_parts: list[str] = [func_name]
        for arg in args:
            key_parts.append(_serialise(arg)[0])
        for k, v in sorted(kwargs.items()):
            key_parts.append(f"{k}={_serialise(v)[0]}")
        cache_name = hashlib.sha256("||".join(key_parts).encode()).hexdigest()
        cache_file = CACHE_DIR / f"{cache_name}.pkl"

        if cache_file.exists():
            try:
                return pickle.loads(cache_file.read_bytes())
            except Exception:
                cache_file.unlink(missing_ok=True)      # corrupt; recompute

        result = func(*args, **kwargs)
        cache_file.write_bytes(pickle.dumps(result))
        return result

    return wrapper
