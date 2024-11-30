import socket

from bit_app.settings.base import *

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
    "127.0.0.1",
    "127.0.0.2",
]

MIDDLEWARE.insert(3, "debug_toolbar.middleware.DebugToolbarMiddleware")
