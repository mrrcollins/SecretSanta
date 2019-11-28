#!/usr/bin/python3

# I have to rewrite the Christmas Drawing script because I can't find the original
# 11/27/2019

import csv,random,os,time
from operator import itemgetter
file = "sample.csv"

print("Christmas Drawing")

everyone = []
group = {}


# Calculate the size of each family group
with open(file) as csvfile:
    members = csv.DictReader(csvfile)
    for row in members:
        g = row['group']
        print("Counting members of family group " + g)

        if g in group:
            n=int(group[g])
            n+=1
        else:
            n=1

        group[g] = str(n)
       
# Put everyone in a list of a dictionary.
total=0
with open(file) as csvfile:
    members = csv.DictReader(csvfile)
    for row in members:
        member = {
                "ID":       total,
                "firstname": row['firstname'],
                "lastname": row['lastname'],
                "email":    row['email'],
                "list":     row['list'],
                "group":    row['group'],
                "size":     group[row['group']],
                "picked":   False,
                }
        total+=1
        everyone.append(member)

# Sort, put the largest family groups first
sorted_e = sorted(everyone, key=itemgetter('size'), reverse=True)

for p in sorted_e:
    pool = []

    for i in everyone:
        if i['group'] != p['group'] and not i['picked']:
            pool.append(i['ID'])

    
    choice = random.choice(pool)
    for i in everyone:
        if i['ID'] == choice:
            i['picked'] = True
            chosen = i

    print(p['firstname'] + " chooses wisely.")
    to = p['email']
    subj = "Your Secret Santa for " + p['firstname']
    file = open("/tmp/email.txt", "w+")
    file.write("Your Secret Santa is: ")
    file.write(chosen['firstname'] + " " + chosen['lastname'] + "\n\n")
    if chosen['list'] !="":
        file.write("Their list is:\n")
    else:
        file.write("They do not have a list.\n")
    file.write(chosen['list'])
    file.close()

    # Debug
    #print(to + " has picked " + chosen['firstname'] + " " + chosen['lastname'])
    command = "mutt -s '" + subj + "' " + to + " < /tmp/email.txt"
    os.system(command)
