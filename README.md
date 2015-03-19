# README #


### Summary ###

* Django Open Calculation Tool
* Version: 0.1

Hive is a project that tries to help other projects that need computation power.
It's a web platform (http://vhb.io), that tries to make high performance cluster
available to anyone.
This project uses docker to run the computation program. This allows to make
the install process very simple and clean. Once the docker container is stopped,
your environment is in the same state than when you launched it.
For now, we just handle Boinc project. But, if you want to make you own project
available too, you just have to make a docker container, and register on our plateform.

Our project tries to cure diseases, study global warming, discover pulsars,
and do many other types of scientific research. It's safe, secure, and easy.
(from Boinc).

http://boinc.berkeley.edu

Please report any bug by an issue.

### Dependencies

You just need to have docker daemon up and running on your computer.
https://www.docker.com

### Want to contribute

You can create your own container and submit it on hive.vhb.io/task/new/

If you want to help us on the plateform development, just fork this project and make
 a pull request.

To run the dev server, just do that :

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py loaddata doct/app/fixtures/tasks.json
    python manage.py runserver

### Who do I talk to? ###

Victor Boudon <vctrhb@gmail.com>
Gary Laurenceau <gary.laurenceau@gmail.com>
