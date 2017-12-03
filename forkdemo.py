
import os
import time
child = os.fork()

if child == 0:

    print 'child started PID:',os.getpid()
    for i in range(10):
        print 'CHILD: value of i=',i

        time.sleep(4)
    os._exit(0)


os.wait()
print 'parent started with pid=',os.getpid()
for j in range(10):
    print 'PARENT: value of j=',j
    time.sleep(1)
#os._exit(0)