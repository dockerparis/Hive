

def generate_configuration(link, ram=1024, cpu=2, gpu=0, disk_space=1024):
    script = "#!/bin/sh\n" \
             "echo 'coucou'\n" \
             "reboot\n"
    return script