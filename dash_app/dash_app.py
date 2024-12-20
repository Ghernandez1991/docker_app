from dash import Dash, dcc, html


def create_dash_app(flask_server):
    """
    Create a Dash app and attach it to the Flask server.
    """
    dash_app = Dash(
        __name__, server=flask_server, url_base_pathname="/dashboard/"
    )  # noqa

    # Dash layout with a static pie chart
    dash_app.layout = html.Div(
        [
            html.H1("Simple Pie Chart", style={"textAlign": "center"}),
            dcc.Graph(
                id="simple-pie-chart",
                figure={
                    "data": [
                        {
                            "type": "pie",
                            "labels": [
                                "Category A",
                                "Category B",
                                "Category C",
                            ],  # noqa
                            "values": [450, 300, 150],
                            "textinfo": "label+percent",
                            "textposition": "inside",
                        }
                    ],
                    "layout": {
                        "title": {"text": "Static Pie Chart", "x": 0.5},
                        "height": 600,
                        "width": 800,
                    },
                },
            ),
        ]
    )

    return dash_app
