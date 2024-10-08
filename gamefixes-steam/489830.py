"""Game fix for Skyrim SE"""

import os
from protonfixes import util


def main() -> None:
    """Run script extender if it exists."""
    if os.path.isfile(os.path.join(os.getcwd(), 'skse64_loader.exe')):
        if 'MODS' in os.environ:
            util.replace_command('SkyrimSELauncher.exe', 'skse64_loader.exe')
