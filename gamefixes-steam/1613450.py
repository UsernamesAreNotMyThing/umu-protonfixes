"""Game fix for Halo 2 mod tools"""

from protonfixes import util


def main() -> None:
    # Requires vcrun2019 to launch
    util.protontricks('vcrun2022')
    util.protontricks('d3dcompiler_47')
    util.protontricks('msxml3')
