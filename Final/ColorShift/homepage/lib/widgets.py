######################################
###   Widgets for our app

from django_mako_plus import render_template
    
class ColorTile(object):
    '''A color widget to be shown on the html page'''
    def __init__(self, title, luma, color):
        self.title = title
        self.luma = luma
        self.color = color
        
    def render(self):
        return render_template(None, 'homepage', 'color_tile.htm', { 'tile': self })