
import pexpect

proc = pexpect.spawn('python sum_of_two.py')

fout = open('sumstatus.log','w')

proc.logfile_read = fout

proc.expect('number:')

proc.send('2\n')

proc.expect('number:')

proc.send('3\n')

proc.expect('sum =  \d+')

r = proc.after

print r

proc.close()
