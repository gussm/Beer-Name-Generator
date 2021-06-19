# Getting user name and greeting the user
user_name = input("What is your name?:\n")
print(f"Welcome to the beer name generator {user_name.capitalize()}!")

# Getting city name.
city_name = input("Why don't you tell me your favorite city?\n")

# Getting season of the year. If not valid, a prompt is printed and information is requested again.
season = input("What is your favorite season of the year?\n")
if season.lower() not in ("spring", "summer", "fall", "winter"):
    print("That is not a valid season. Please choose between: Spring, Summer, Fall, Winter")
    input("What is your favorite season of the year?\n")

# Getting weather info. If not valid, same as before, a prompt is printed and information is requested.
weather = input("Do you like wet, dry, hot or humid weather?\n")
if weather.lower() not in ("hot", "wet", "dry", "humid"):
    print("That is not a valid weather type. Please choose between: Wet, Dry, Hot, Humid")
    input("Do you like wet, dry, hot or humid weather?\n")

# Getting pet name.
pet_name = input("What about your favorite type of animal?\n")

# Getting beer type. If not available, prompt is shown, and info requested.
beer_type = input("Finally, what is your favorite type of beer?\n")
if beer_type.lower() not in ("ale", "lager", "porter", "stout"):
    print("That is not a valid beer type. Please choose between: Ale, Lager, Porter, Stout")
    input("Finally, what is your favorite type of beer?\n")

# Finally the beer name generator provides a recommendation to the user.
print(f"{user_name.capitalize()}, the beer generator program would like to recommend you to name your beer:\n "
      f"\"{city_name.capitalize()}'s {season.capitalize()} {weather.capitalize()} "
      f"{pet_name.capitalize()} {beer_type.capitalize()}\"")
