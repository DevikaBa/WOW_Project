import pandas as pd 

music_data = pd.read_csv('familiar_music_database.csv')

# print first 5 rows
print(music_data.head())

# get the shape of the data frame
print(music_data.shape)


print(music_data.columns)

# selecting the columns
music_data = music_data[['year', 'title', 'artist', 'genre']]

# selecting row
#print(music_data[music_data.genre == 'elvis'])

# function to take user input for the desired song genre
# then output a dataframe of songs of that genre only
def filter_by_genre():
    # print the unique genres
    print(music_data.genre.unique())

    # takes user input
    user_input_genre = input('What genre do you want? ')

    # filter the data based on the user input
    filtered_data = music_data[music_data.genre == user_input_genre]

    # return the output dataframe
    return(filtered_data)


# run the function
print(filter_by_genre())
