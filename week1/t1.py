from audioop import reverse
from typing import List


L1 = [(), ('hehe', 'i-am-ded-inside'),
      ('suitcase-memes.exe'), (), 'kill me plis']
L1.reverse()
rem = filter(None, L1)


print(list(rem))
