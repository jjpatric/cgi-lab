#!/usr/bin/env python3

import os
import json

my_env = dict(os.environ)
json_env = json.dumps(my_env)

print("Content-Type: text/plain")
print()
print(json_env)
#print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}<\p>")