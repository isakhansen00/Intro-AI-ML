import re

strings = "dette-er;entest"

split_string = re.split(r"-|;|\s", strings)

new_split = re.split(r"[-;,.\s]\s*", strings)

print(split_string)
print(len(split_string),"\n")

print(new_split)