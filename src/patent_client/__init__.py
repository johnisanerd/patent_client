# flake8: noqa
import json
import os
import shutil
import time
from pathlib import Path

__version__ = "0.4.1"


CACHE_BASE = Path("~/.patent_client").expanduser()
CACHE_BASE.mkdir(exist_ok=True)
CACHE_MAX_AGE = 60 * 60 * 24 * 3  # 3 days
now = time.time()
# Clear old files out of cache
for path, folders, files in os.walk(CACHE_BASE):
    for f in files:
        fname = os.path.join(path, f)
        if now - os.path.getmtime(fname) > CACHE_MAX_AGE:
            os.remove(fname)

SETTINGS_FILE = Path("~/.iprc").expanduser()
if not SETTINGS_FILE.exists():
    DEFAULT_SETTINGS = Path(__file__).parent / "default_settings.json"
    shutil.copy(str(DEFAULT_SETTINGS), SETTINGS_FILE)

SETTINGS = json.load(open(SETTINGS_FILE))

from patent_client.epo_ops.models import Inpadoc, Epo  # isort:skip
from patent_client.uspto_assignments import Assignment  # isort:skip
from patent_client.uspto_exam_data.main import USApplication  # isort:skip
from patent_client.uspto_ptab import PtabDocument  # isort:skip
from patent_client.uspto_ptab import PtabTrial  # isort:skip
from patent_client.itc_edis import (
    ITCInvestigation,
    ITCDocument,
    ITCAttachment,
)  # isort:skip
