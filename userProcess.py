import subprocess
users = {}
ps_cmd = subprocess.check_output(['ps','-ef'])
for line in ps_cmd.splitlines()[1:]:
    user = line.split()[0]
    users[user]=users.get(user,0)+1
print users
