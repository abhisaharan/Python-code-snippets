import logging
import re

logging.basicConfig(filename='deprecation.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

s = "this is my address and yours address"
pattern = r'\baddress\b'
a = re.sub(pattern, 'name.address', s)
print(a)