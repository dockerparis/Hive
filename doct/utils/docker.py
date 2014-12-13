

def generate_configuration(link, ram=1024, cpu=2, gpu=0, disk_space=1024):
    script = "#!/bin/bash\n" \
                "if [ $# -eq 0 ]\n" \
                "then\n" \
                    "echo 'No url supplied' \n" \
                    "exit 0\n" \
                "fi\n" \
                "read -p 'Name: ' name\n" \
                "read -p 'Mail: ' mail\n" \
                "read -s -p 'Enter password: ' password\n" \
                "result=\"`boinccmd --create_account $1 $mail $password $name`\" \n" \
                "key=\"`echo $result| grep 'account key' | rev | cut -d':' -f1 | rev`\" \n" \
                "echo \"url: \" $1\n" \
                "echo \"key: \" $key\n" \
                "boinc --attach_project $1 $ke\n"
    return script