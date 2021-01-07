
class chartTemplate:
    def __init__(self, text=''):
        annotations = [dict(xref='paper', yref='paper',
                            x=0, y=1.05,
                            xanchor='left', yanchor='bottom',
                            text=text,
                            font=dict(size=20),
                            showarrow=False)]
        self.layout = dict(annotations=annotations,
                            plot_bgcolor='#f3f4f7',
                            xaxis = dict(linecolor='gray', linewidth=2),
                            yaxis = dict(linecolor='gray', linewidth=2))