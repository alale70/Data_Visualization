'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    
    # create empty figure by plotly express 
    fig = px.line(x = [0,0], y = [0,0])
    # Display text
    fig.update_layout(dragmode = False,
                      yaxis = {'visible': False, 'showticklabels': False},
                      xaxis = {'visible': False, 'showticklabels': False})
    fig.add_annotation(text = "No data to display. Select a cell in the heatmap for more information", 
                       showarrow = False)
    # place text at the center of the figure
    fig.update_annotations(xref = "paper",yref = "paper", font_family = THEME['accent_font_family'])
    return fig  


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    # Display rectangle with 0.25 to 0.75 of the heigh
    fig.add_shape(type = "rect", 
                  fillcolor = THEME['pale_color'],
                  line_color = THEME['pale_color'],
                  opacity = 1,
                  xref = "x domain", 
                  yref = "y domain", 
                  x0 = 0, x1 = 1, y0 = 0.125, y1 = 0.875)
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template

    # Find number of non-zero elemnts
    column = line_data['Counts'].values
    count = 0
    for el in column:
        if el!= 0: 
            count += 1
            
    # Use scatter plot insted of line for one data
    if count != 1:
        fig = px.line(line_data, x = "Date_Plantation", y = "Counts")

    else:
        fig = px.scatter(line_data, x = "Date_Plantation", y = "Counts")
        
    
    # setting hover template for line chart
    fig.update_traces(hovertemplate = hover_template.get_linechart_hover_template())

    # Update title by value of arround and year
    # Display xaxis just by month and day without year
    fig.update_layout(title = f"Trees planted in {arrond} in  {year}",
                      xaxis_title = " ",
                      yaxis_title = " Trees ", 
                      xaxis=dict(tickformat="%d %b"))

    return fig
