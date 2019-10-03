import dash
from dash import no_update
from dash.dependencies import Input,Output,State
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from utilities import fetchilarity_score

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    dcc.Markdown(
'''
# Fetchilarity

### Enter two bits of text to determine how similar they are!

Made with love by Russell.

'''
                    ),
                ),
                style=dict(textAlign='center')

            ),

            dbc.Row(
                [
                    # enter text1
                    dbc.Col(
                        [
                            dbc.Textarea(placeholder='Enter the first bit of text',id='text1'),
                        ],
                        width=6
                    ),
                    # enter text2
                    dbc.Col(
                        [
                            dbc.Textarea(placeholder='Enter the second bit of text',id='text2'),
                        ],
                        width=6
                    )
                ]
            ),
            html.Br(),

            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button('SUBMIT',id='submit',color='primary',size='lg',block=True,n_clicks=0)
                    ),
                ],
            ),
            html.Br(),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(id='output',style=dict(textAlign='center'))
                        ]
                    )
                ]
            )
        ]
    )
])




@app.callback(
    Output('output','children'),
    [Input('submit','n_clicks')],
    [State('text1','value'),
     State('text2','value')]
)
def get_score(n_clicks,text1,text2):
    if n_clicks==0:
        return no_update

    try:
        score = fetchilarity_score(text1,text2,mode='api')
    except BaseException as e:
        print(text1,text2)
        print(e)
        return 'something went terribly wrong with that input. Please try again.'
        

    return dbc.Card(
        [
            html.H3('Fetchilarity Score',className='card-title'),
            html.H1(str(round(score,4)))
        ],
        body=True
    )



if __name__ == "__main__":
    app.run_server(
        port=8050,
        debug=True
    )