import os

addr = "nohup uwsgi --socket expense.sock --module Expense_Track.wsgi --chmod-socket=666 &"
command =  "ps aux | grep \"" + addr  + "\""

pid = os.popen(command).read()
print(pid)

print(os.system("kill " + pid))
