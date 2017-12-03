

n = 121
m = n
rev = 0

while n!=0:
	d= n % 10
	rev = rev * 10 + d
	n= n /10
print "Reverse of a number = " ,rev
if m==rev:
  print "Given number is Palindrome"
else:
  print "Given number is not a palindrome"