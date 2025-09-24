user_name = input("Enter your full name (First, Middle, Last): ")
format_name = user_name.strip().split()
first_name = format_name[0].title()
last_name = format_name[2].title()
middle_name = format_name[1].title()
middle_initial = middle_name[0]+"."
print(last_name + ", " +  first_name + " " + middle_initial)
