from time import sleep

def countdown(n):
  # pre-condition: n must be a positive integer
  # post-condition: countdown from n to 1 then print blastoff!
  #                 exit on n == 0

  # Exit Condition
  if n == 0:
    print("Blastoff!")
  else:
    print(n)
    sleep(1)        # sleep for 1 second
    countdown(n-1)  # recursive call. Go from n to n - 1.

## Main Program ##
countdown(10)
