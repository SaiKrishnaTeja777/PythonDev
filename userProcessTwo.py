import subprocess
users = {}
ps_cmd = subprocess.check_output(['ps','-ef'])
for line in ps_cmd.splitlines()[1:]:
    user = line.split()[0]
    if users.get(user):
       users[user]+=1
    else:
       users[user]=1

print "Active users on the system are " + ','.join(users.keys())
for user, process_count in users.items():
    print "%s is running %s processes" % (user, process_count)

print users
del users['root']
print users
