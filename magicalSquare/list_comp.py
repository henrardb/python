#!/usr/bin/env python3

logs_bruts = [
    "INFO: User 'bruno' logged in from 192.168.1.10: Success",
    "ERROR: Failed to connect to DB on port 5432.",
    "INFO: Server status nominal.",
    "WARNING: Disk usage at 85% on /var/log.",
    "ERROR: Permission denied for user 'root' on /etc/shadow.",
    "INFO: Task scheduler finished successfully."
]

erreurs_critiques = [
          line 
          for line in logs_bruts
          if "ERROR" in line
        ]

#print(erreurs_critiques)

premier_mot = [
        mot.split(":")[0]
        for mot in logs_bruts
        ]   
#print(premier_mot)

data = [ 
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ],
    ]

sortie_data = [
            sum(line[col] for line in data)
            for col in range(len(data[0]))
        ]

#print(sortie_data);

mat = [[1,2], 3, [3,4]]

nombres_plats = [
        n
        for elmnt in mat
        for n in (elmnt if isinstance(elmnt, list) else [elmnt]) 
        ]

print(nombres_plats)
