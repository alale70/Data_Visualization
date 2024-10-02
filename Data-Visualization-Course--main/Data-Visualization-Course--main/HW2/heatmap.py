'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template



def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick.

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''
   


    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    
    # Display the heatmap same as the refered figure of the pdf
    fig = px.imshow(data, 
                    labels = dict(color="Trees",x="",y=""), 
                    x = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
    fig.update_traces(hovertemplate = hover_template.get_heatmap_hover_template())
    fig.update_layout(dragmode = False)
    fig.update_xaxes(dtick = 1)
    return fig
