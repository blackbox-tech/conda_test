import os, sys, yaml
from pathlib import Path

def share_dir():
    """
    # This will resolve to the shared data dir under the current PYTHONPATH or CONDA_PREFIX if it exists
    """
    mod_path = Path(__file__)
    share_path = mod_path.parent.parent.parent / "share"
    if share_path.is_dir():
        return share_path
    try:
        mod_path.relative_to(os.environ.get("CONDA_PREFIX"))
        share_path = mod_path.parent.parent / "share"
        if share_path.is_dir():
            return share_path
    except:
        pass # this module is not under CONDA_PREFIX
    raise FileNotFoundError("share directory not found, set your PYTHONPATH or activate your conda environment")

def message():
    with open(share_dir() / "test_data.yml" , "rt") as fh:
        config = yaml.safe_load(fh)
    return config["message"]