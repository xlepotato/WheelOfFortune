'''
First, let's learn about a few functions and methods that we'll use along the way to do this project.
There are no questions to answer in the next four active code windows. They are just here to introduce you to some
functions and methods that you may not be aware of. The active code window that starts with “Part A” is where you are
first asked to complete code.

----------------------------------------

The time.sleep(s) function (from the time module) delays execution of the next line of code for s seconds.
You'll find that we can build a little suspense during gameplay with some well-placed delays. The game can also be
easier for users to understand if not everything happens instantly.
'''
import time

for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(x) # "Sleep" for x seconds
print('Done!')
