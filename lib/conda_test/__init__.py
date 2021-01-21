import os, sys, yaml
from pathlib import Path

def share_dir():
    """
    # This will resolve to the shared data dir under the current PYTHONPATH or CONDA_PREFIX if it exists
    """
    path = Path(__file__).parent / "../../share"
    if path.is_dir():
        return path
    conda_env = os.environ.get("CONDA_PREFIX")
    if conda_env:
        return Path(conda_env) / f"lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages/share"
    raise FileNotFoundError("share directory not found, set your PYTHONPATH or activate your conda environment")

def message():
    with open(share_dir() / "test_data.yml" , "rt") as fh:
        config = yaml.safe_load(fh)
    return config["message"]