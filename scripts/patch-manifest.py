#!/usr/bin/env python3
"""Inject android:usesCleartextTraffic="true" into <application> so the
Tailscale FORGE endpoint (http://100.84.104.65:8080) is reachable from the APK."""
import re, sys

path = sys.argv[1]
xml = open(path, encoding="utf-8").read()
if 'usesCleartextTraffic' in xml:
    print("already set"); sys.exit(0)
xml, n = re.subn(r"<application\b", '<application android:usesCleartextTraffic="true"', xml, count=1)
if n != 1:
    sys.exit("could not find <application> element in " + path)
open(path, "w", encoding="utf-8").write(xml)
print("cleartext traffic enabled in", path)
