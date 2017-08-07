def has_letter_e(self):
    letter = [letter for letter in self]
    if "e" in letter:
      return True
    else:
      return False
x = "home"
y = "car"
z = "University"

print has_letter_e(x)
print has_letter_e(y)
print has_letter_e(z)
