#!/usr/bin/env python
from helpers.strings import extract_lower
from helpers import variables
from helpers import *
import helpers


print(f"Lowercase Letters: {extract_lower(variables.name)}")
print(f"Uppercase Letters: {extract_upper(variables.name)}")

print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")