import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'public-apis', 'youtube-dl']

plot_dicts = [
    {'value': 50908, 'label': 'Description of awesome-python'}, 
    {'value': 37595, 'label': 'Description of public-apis'}, 
    {'value': 37513, 'label': 'Description of youtube-dl'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')