user_favmovies = []

user_ans = input("What's your favorite movie? ")
print(user_ans,' has been added to the list')
user_favmovies.append(user_ans.title())

user_ans2 = input("What's your favorite movie? ")
print(user_ans2,' has been added to the list')
user_favmovies.append(user_ans2.title())

user_ans3 = input("What's your favorite movie? ")
print(user_ans3,' has been added to the list')
user_favmovies.append(user_ans3.title())

print("Your favorite movies are:", user_favmovies[0], user_favmovies[1], user_favmovies[2])

