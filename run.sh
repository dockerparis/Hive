#!/bin/sh
# Boinc cointainer run script
# Copyright (C) 2014 vhb
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# creer loopback
#   truncate -> truncate 10G run
#   format mount
# docker run -v volume

# --cpus={:s} --cpu-share={:s} --storage-opt={:s}

usage() {
    echo "usage : cpu_count cpu_shares memory disk project_url"
    exit 1
}

if test $# -eq 0; then
    usage
else
    if test "$#" -ne 5 ; then
        usage
    fi
fi

#if ! type "losetup" > /dev/null; then
    #echo "losetup unavalaible: space disk will not be controlled"
    #docker run --cpu-share=$cpu_shares --cpus=$cpu_count \
        #$container_name $project_url
#else
    #echo $disk
    #dd if=/dev/zero of=lvmtest0.img bs=1 count=$disk
    #for i in {8..63}; do 
        #if [ -e /dev/loop$i ];
        #then
            #continue; 
        #fi;
        #echo $i
        #truncate --size $disk lvmtest0.img
        #mknod /dev/loop$i b 7 $i;
        #losetup lvmtest0.img
        #chown --reference=/dev/loop0 /dev/loop$i;
        #chmod --reference=/dev/loop0 /dev/loop$i; 
        #sudo mkfs.ext4 /dev/loop$i
        #sudo mount /dev/loop$i /var/lib/docker_boinc
        #break;
    #done

    cpu_count=$1
    cpu_shares=$2
    memory=$3
    disk=$4
    project_url=$5
    volume=/var/lib/docker_boinc
    container_name='test'

    nb_cpu=$(nproc)
    cpu_option='0'
    i=1
    while [ $i -lt $nb_cpu ]; do
        if [[ i -gt $cpu_count ]]; then
            break
        fi
        cpu_option+=",$i"
        i=$[$i+1]
    done
    #echo $cpu_option
    docker run -v $volume -c=$cpu_shares --cpuset=$cpu_option \
        $container_name $project_url
#fi

