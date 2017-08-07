#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plistlib
import subprocess
import re
from datetime import timezone
from os import listdir, mkdir
from os.path import isfile, isdir, join, splitext

ENTRIES_DIR = 'entries'
entry_files = [f for f in listdir(ENTRIES_DIR) if
        isfile(join(ENTRIES_DIR, f)) and splitext(f)[1] == '.doentry']

for fn in entry_files:
   print(fn)
   with open(join(ENTRIES_DIR, fn), 'rb') as fp:
       entry = plistlib.load(fp, fmt=plistlib.FMT_XML)

       # Bring the entry creation time into local timezone, which
       # is what SetFile expects.
       ctime = entry['Creation Date'] \
               .replace(tzinfo=timezone.utc) \
               .astimezone(tz=None)

       # Using raised colon (˸) instead of standard colon here because
       # macOS doesn't treat standard colons well in filenames
       new_entry_dir = join('md', ctime.strftime('%Y'))
       if not isdir(new_entry_dir):
           mkdir(new_entry_dir)
       new_entry_fn = join(new_entry_dir, ctime.strftime('%B %d, %Y %H˸%M') + '.md')

       with open(new_entry_fn, 'w') as new_entry:
           # Remove all blank lines, because Ulysses treats them
           # as paragraph breaks
           entry_lines = entry['Entry Text'].split('\n')
           entry_text = str.join('\n',
               [entry_line for entry_line in entry_lines if entry_line != '']
           )

           new_entry.write(entry_text)

           # Set the creation time.
           subprocess.call("SetFile -d \"{:%m/%d/%Y %H:%M:%S}\" {}".
                   format(ctime, re.sub(r' ', '\ ', new_entry_fn)), shell=True)
