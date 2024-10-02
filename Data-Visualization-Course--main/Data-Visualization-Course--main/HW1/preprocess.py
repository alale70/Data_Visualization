'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    
    # drop Scene and PlayerLine Column
    my_df.drop(['Scene', 'PlayerLine'], axis = 1, inplace = True)

    #creating group for each Act and Player and then creating a column named 'LineCount' for summing each player’s line count for the act
    grouped_df = my_df.groupby(['Act', 'Player']).agg(LineCount = ('Line', 'count')).reset_index()  
    
    #adding LinePercent column to the dataframe
    grouped_df['LinePercent'] = 100 * grouped_df['LineCount'] / grouped_df.groupby(['Act'])['LineCount'].transform('sum')


    return grouped_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    
    #First : we will find the 5 top player in all acts

    #keeping a copy of the dataframe
    copy_df = my_df.copy()

    #group all acts of players and calculating line count for each player for all acts
    #sort Line Counts in descending order
    ff = copy_df.groupby(['Player'])['LineCount'].sum().reset_index().sort_values(by = ['LineCount'], ascending = False).reset_index(drop = True)
    #get the 5 top player
    five_tops = ff['Player'].loc[0:4][:]
    

    #query from the dataframe to get 5 top players in the dataframe
    five_top_df = copy_df.query("Player in @five_tops")
    
    #query from the dataframe to get other players than 5 top players in the dataframe
    other_df = copy_df.query("Player not in @five_tops")
    #get the summation of line count and line percent for each act for the "other" category
    other_df = other_df.groupby(['Act']).sum().reset_index()
    #inserting the column player for the "other" category
    other_df.insert(0, "Player", 'Other')

    #concating the five top player and other category then sort them according to the act
    my = pd.concat([five_top_df, other_df], axis = 0, ignore_index = True).sort_values(by = ['Act'], ascending = True).reset_index(drop = True)

    return my


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    
    my_df['Player'] = my_df['Player'].str.capitalize()
    my_df.reset_index(drop = True)
    return my_df
