'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating the hovered element's x value, with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * A bold label for the player name followed
                by the hovered elements's player's name
            * A bold label for the player's lines
                followed by:
                - The number of lines if the mode is 'Count'
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent'.

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''
    # TODO: Generate and return the over template
    if mode == 'Count': 
        tool = """<span style='font-family:Grenze Gotish; font-size:24px; color:Black;'>%{x}<br /><br /></span><b>Player :</b>""" + name +"""</span><br /><b>Lines :</b> %{y}</span>"""
        
    else:
        tool = """<span style='font-family:Grenze Gotish; font-size:24px; color:Black;'>%{x}<br /><br /></span><b>Player :</b>""" + name +"""</span><br /><b>Percent :</b> %{y:.2f}%</span>"""
        
    return tool
