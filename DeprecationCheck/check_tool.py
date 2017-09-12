import os
import optparse
import logging
import re
import DeprecationCheck.file1
import DeprecationCheck.file2
import DeprecationCheck.file3
import DeprecationCheck.file4
import DeprecationCheck.file5

logging.basicConfig(filename='deprecation.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

file1_doc = dir(DeprecationCheck.file1.__str__)
print(file1_doc)
a = re.sub(r'\baddress\b', 'name.address', file1_doc)
print(a)