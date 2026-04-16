# Guide to deploying your own Gemini server

### Create a virtual environment and enter it
``` shell
python -m venv venv

. venv/bin/activate
```

### Install Jetforce
``` shell
pip install jetforce
```

### Create folders for content and certs (optional)
``` shell
mkdir certs content
```

### Create a certificate
```
openssl req -newkey rsa:4096 -sha256 -nodes -keyout certs/<YOUR_DOMAIN>.key -nodes -x509 -out certs/<YOUR_DOMAIN>.crt -s
ubj "/CN=<YOUR_DOMAIN>" --days <NUMBER_OF_DAYS>
```

### Create jetforce.sh
```
#!/bin/sh
. venv/bin/activate && jetforce --dir content/ --host <YOUR_SERVER_IP> --port 1965 --hostname <YOUR_DOMAIN> --tls-certfile
 certs/<YOUR_DOMAIN>.crt --tls-keyfile certs/<YOUR_DOMAIN>.key
```
More parameters can be found here: https://github.com/michael-lazar/jetforce?tab=readme-ov-file#usage


### Create /etc/systemd/system/jetforce.service
```
[Unit]
Description=Jetforce Gemini server

[Service]
WorkingDirectory=<PATH_TO_DIRECTORY_WITH_SCRIPT_FROM_ROOT>
ExecStart=sh jetforce.sh
Restart=always
RestartSec=3
User=<USERNAME>

[Install]
WantedBy=multi-user.target
```

### Run the server
``` shell
systemctl start jetforce
```

# Used software

| name     | license                        | site                                      |
|---       |---                             |                                           |
| Jetforce | Floodgap Free Software License | https://github.com/michael-lazar/jetforce |