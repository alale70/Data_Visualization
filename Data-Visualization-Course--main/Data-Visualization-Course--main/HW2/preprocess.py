'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    # Convert the value of 'Date_plantation' in the dataframe to datetime objects
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    
    # Filters the value of 'Date_Plantation' in the dataframe by date.
    # For this purpose, we can access the 'Date_Plantation' column by a boolean array.
    dataframe = dataframe.loc[(dataframe['Date_Plantation'] >= ('%d-01-01' % start))& (dataframe['Date_Plantation'] <= ('%d-12-31' % end))]
    
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    
    # Creating group for each neighborhood and year and then counting the number of trees in these categories.
    # Put the name of the 'Count' on existing column.
    yearly_df = dataframe.groupby([dataframe['Arrond_Nom'],dataframe['Date_Plantation'].dt.year]).size().reset_index(name='Counts')
    return yearly_df


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0

    # Createing a spreadsheet-style pivot table as a DataFrame.
    data = yearly_df.pivot_table('Counts', ['Arrond_Nom'], 'Date_Plantation')
    
    # Filling empty cells with zeros
    data = data.fillna(0)
    
    # Renaming columns with the string date
    data = data.rename({2010: '2010-12-31', 2011: '2011-12-31', 2012: '2012-12-31', 2013: '2013-12-31',
                       2014: '2014-12-31', 2015: '2015-12-31', 2016: '2016-12-31', 2017: '2017-12-31',
                       2018: '2018-12-31', 2019: '2019-12-31', 2020: '2020-12-31'}, axis=1)
    return data


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return

    # Filters the value of 'Date_Plantation' by the specified year and 'Arrond_nom' by the specified neighborhood.
    df1 = dataframe.loc[(dataframe['Date_Plantation'] >= ('%d-01-01' % year))& (dataframe['Date_Plantation'] <= ('%d-12-31' % year))&
                        (dataframe['Arrond_Nom'] == arrond)]
    
    # Getting the daily amount of planted trees and then creating group.
    df1 = df1.groupby(pd.Grouper(key='Date_Plantation',freq='1D')).count().reset_index(drop=False, inplace=False).rename({'Arrond': 'Counts'}, axis=1)
    df1 = df1.fillna(0)
    # Drop the neighborhood, longitude and latitude columns
    line_data = df1.drop(['Arrond_Nom', 'Longitude','Latitude'], axis=1)
    return line_data
