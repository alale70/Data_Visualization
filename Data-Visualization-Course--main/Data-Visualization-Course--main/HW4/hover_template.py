'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    # Display the neighborhood's name by customdata=locations
    return "<span style='font-family:Oswald'> %{customdata}<br /></span><extra></extra>"""


def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    # Display the name as a string in the tooltips
    return """<span style='font-family:Oswald'>"""+ name +"""<br /></span><extra></extra>"""