'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio


from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title

    fig.update_layout(
        template = pio.templates['simple_white'],
        dragmode = False,
        barmode = 'relative'
    )
    
    #setting the tempalte and title
    fig = go.Figure(layout = go.Layout(title="Lines per act"))
    pio.templates.default = 'simple_white+custom'
    fig.update_layout(template = pio.templates.default, title = "Lines per act")
    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode
    df = data.copy()   #keeping a copy of the data
    df = df.assign(Act = 'Act' + ' ' + df.Act.apply(str))   #to assign an appropriate x labels
    
    
    #Plotting the bar chart based on the current mode and calling the "get_hover_template" for the tooltip
    if mode == 'Count':
        data = [go.Bar(name = Player, x= dfg['Act'], y=dfg['LineCount'], 
                       hovertemplate= get_hover_template(Player,mode)) for Player, dfg in df.groupby(by='Player')]

        # plot the figure
        fig = go.Figure(data)
        fig.update_layout(barmode='stack', title='Lines per act')

    else:  
        data = [go.Bar(name = Player, x= dfg['Act'], y=dfg['LinePercent'], 
                       hovertemplate=get_hover_template(Player,mode)) for Player, dfg in df.groupby(by='Player')]

        # plot the figure
        fig = go.Figure(data)
        fig.update_layout(barmode='stack', title='Lines per act')

    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    if mode == 'Count':
        fig.update_yaxes(title_text='Lines (Count)')
    else:
        fig.update_yaxes(title_text='Lines (%)')