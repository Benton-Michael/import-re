import re

# check the text entered to see if it matches the pattern of our regex. Return a message to the user regarding a match or no match.
# In this example, we will check to see if the string entered begins with the word "The" and ends with the word "world".

txt = "The best programming language in the world"
x = re.search("^The.*world$, txt)
              
if x:
   print("There is a match")
else:
   print("No match")
