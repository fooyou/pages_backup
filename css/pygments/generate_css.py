import os
from pygments.styles import STYLE_MAP

for style in STYLE_MAP.keys():
    os.system('pygmentize -S ' + style + ' -f html > ' + style + '.css')
