# MOVIE RECCOMENDATION SYSTEM
# Build a movie reccomendation system that will suggest movies to users based on their preferences and previously watched movies
# the programme should read a file containing a list of previously watched movies and their genres
# and reccomend movies based on the values in the file 
# be sure to utilize exception handeling and write unit tests

import string

def recommend_movie():
    try:
        with open("watched_movies.txt", "r") as watched_file: # reads the watched movies file
            watched_movies = watched_file.readlines() # readlines() allows the file to be read line by line and stored in a list

            with open("recommended_movies.txt", "r") as redommended_file:
                recommend_movie = redommended_file.readlines() # this reads the recommended movies file

            watched_genres = [line.strip().split(" - ")[1].lower() for line in watched_movies] # this splits it at genre and makes a new list of watched genres

            recommendations = [] # assign recommendations as empty list
            for movie in recommend_movie:
                already_watched, genre = movie.strip().split(" - ") # .strip() removes whitespace // .split() splits at the specified place
                if genre.lower() in watched_genres:
                    recommendations.append(movie.strip())
            
            if recommendations:
                print("\nBased on your watched movies, we recommend:")
                for movie in recommendations:
                    print(movie)
            
            else:
                print("Sorry, we returned no recommendations")

    except FileExistsError:
        print("Error: One or more files not found")
    except Exception as e:
        print(f"An error occured: {e}")


def add_movie():
    already_watched = input("What movie do you want to add to the watched list?\n").strip()  # Normalize input
    genre = input("What is the genre?\n").strip()
    
    with open("watched_movies.txt", "a") as file:
        file.write(f"{already_watched} - {genre}\n")
    
    print(f"{already_watched} has been added to your watched list")


def main():
    # Ask user if they want to be recommended or add an movie 
    choice = input("Do you want to be recommended a movie or add a movie to your watch list? (Type 'recommended' or 'add')\n").strip().lower()
    if choice == "recommend":
        recommend_movie()
    elif choice == "add":
        add_movie()
    else:
        print("Invalid choice. Please type 'recommend' or 'add'.")

main()