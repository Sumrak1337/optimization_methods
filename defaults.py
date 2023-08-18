import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.absolute()
CONFIGS_ROOT = PROJECT_ROOT / 'configs'
METHODS_ROOT = PROJECT_ROOT / 'methods'
RESULTS_ROOT = PROJECT_ROOT / 'results'

os.makedirs(RESULTS_ROOT, exist_ok=True)
