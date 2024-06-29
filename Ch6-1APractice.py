##Robert Fernandez
##Complete
####Write a file with your name, someone else's name, and your age.

def main():

  # Creates file to open and write to
  file = open("my_name.txt", "w")

  # Writes lines to the file to display
  file.write("Robert Fernandez\n")
  file.write("Joseph Fernandez\n")
  file.write("33\n")

  # Closes the file
  file.close()

if __name__ == "__main__":
  main()
