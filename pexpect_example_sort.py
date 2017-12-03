
import pexpect

proc = pexpect.spawn('sort')

fout = open('soutstatus.log','w')
proc.logfile_read =fout

data = ['hello', 'hi','ok','done','apple']
()

for msg in data:

    proc.send(msg+'\n')

proc.sendcontrol('d')

proc.expect(pexpect.EOF)

proc.close()
