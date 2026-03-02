import importlib

from . import samplers, schedulers, trainers


def __getattr__(name: str):
    if name != "eval":
        raise AttributeError(f"module 'dllm.core' has no attribute {name!r}")
    try:
        return importlib.import_module(".eval", __name__)
    except ModuleNotFoundError as exc:
        if exc.name != "lm_eval":
            raise
        raise ModuleNotFoundError(
            "The optional evaluation dependency is not installed. "
            "Run `uv sync --group evaluation` to enable lm-evaluation-harness."
        ) from exc


__all__ = ["samplers", "schedulers", "trainers", "eval"]
