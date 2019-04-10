import platform as osinfo

os_s = ["architecure", "machine", "node", "processor", "system", "system_alias(system, release, version)", "version", "dist", "linux_distribution"]

for key in os_s:
    if hasattr(osinfo, key):
        print(key + " - " + str(getattr(osinfo, key)()))
