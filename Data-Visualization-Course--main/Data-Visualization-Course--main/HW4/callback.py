'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    if style['visibility']=='hidden':
        return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    if style['visibility']=='hidden':   #it means the panel was hidden before
        return None, None, None, style   #So, panel still will not show up
    else:              #it means panel was visible before
        return title, mode, theme,style     #So, panel will display as before


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
    #set style:
    style = {'visibility': 'visible','border': '1px solid black', 'padding': '10px'}
    
    #set title
    color = figure['data'][curve]['marker']['color']      #Find the color of the marker
    title_text = figure['data'][curve]['customdata'][point][0]   #Find the title text to display
    title = [html.Span(title_text , style={'color': color,'fontWeight': 'bold'})]  #set the title text color and foint weight 
    
    #set mode 
    mode_text = figure['data'][curve]['customdata'][point][2]   #Find the mode text to display
    mode = [html.Span(mode_text, style={'fontWeight': 'bold'}), html.Span("\n")]  #set the mode text as bold
    
    #set theme
    theme_text = figure['data'][curve]['customdata'][point][1]  #Find theme text to display
    if theme_text:  #check if theme text is empty or not
        theme_l = list(theme_text.split('\n'))    #break the theme text by "\"
        theme = [html.Span("Thématique:"), html.Ul(children=[html.Li(l) for l in theme_l])]  #Display the theme as it was asked
    else:
        theme = None   #theme text is empty                               
    
    return title, mode, theme,style
