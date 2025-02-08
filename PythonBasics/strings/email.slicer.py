email =input()

index =email.find('@')

userName =email[:index]
domain =email[index+1:]

print(f"Your Username is {userName} and domain is {domain} ")