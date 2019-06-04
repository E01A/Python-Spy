#!/bin/bash
#

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1
 if [ $? -eq 0 ]; then
       apt-get install python-pip
       pip install -r requirements.txt
       interface="$(/bin/ip route | awk '$1 == "default" {for (i=2;i<=NF;i++) if ($i == "dev") { i++;print $i; exit}}')"
       if /sbin/iw dev "$interface" info &>/dev/null; then   
            python wi.py
            sleep 60m
            ( exec "inf.sh" )      

           
       else 

           python et.py
           sleep 60m
           ( exec "inf.sh" ) 

       fi

 else
   sleep 10m
   ( exec "inf.sh" )

 fi




