import sys
if sys.version > '3':
    PY3 = True
else:
    PY3 = False
from .uarm import UArm, get_uarm, get_default_logger, UArmConnectException, home_dir, ua_dir
from .version import __version__
