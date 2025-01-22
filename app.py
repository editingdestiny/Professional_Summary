from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# List of available DBC themes
themes = {
    "Cerulean": dbc.themes.CERULEAN,
    "Cosmo": dbc.themes.COSMO,
    "Cyborg": dbc.themes.CYBORG,
    "Darkly": dbc.themes.DARKLY,
    "Flatly": dbc.themes.FLATLY,
    "Journal": dbc.themes.JOURNAL,
    "Litera": dbc.themes.LITERA,
    "Lux": dbc.themes.LUX,
    "Minty": dbc.themes.MINTY,
    "Pulse": dbc.themes.PULSE,
    "Sandstone": dbc.themes.SANDSTONE,
    "Simplex": dbc.themes.SIMPLEX,
    "Sketchy": dbc.themes.SKETCHY,
    "Slate": dbc.themes.SLATE,
    "Solar": dbc.themes.SOLAR,
    "Spacelab": dbc.themes.SPACELAB,
    "Superhero": dbc.themes.SUPERHERO,
    "United": dbc.themes.UNITED,
    "Yeti": dbc.themes.YETI,
}

# Initialize the app with a default theme
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# App layout
app.layout = html.Div([
    # Dropdown for theme selection (top-right corner)
    html.Div(
        dcc.Dropdown(
            id="theme-selector",
            options=[{"label": theme, "value": url} for theme, url in themes.items()],
            value=dbc.themes.LUX,  # Default theme
            clearable=False,
            style={"text-align": "justify","width": "200px", "float": "right", "margin": "10px"},
        ),
    ),

    # Main content
    dbc.Container([
        # Name section
        html.Div([
			    html.Br(),
            html.H1("Sudhanshu Deo", className="text-center"),
	    html.Br(),

            html.P(
                "With 16+ years of experience in Tier-I investment banks, I am a techno-functional leader specializing in Data Governance, Regulatory Change, Payments, and Capital Markets. Currently a Data integration manager Programme Manager, they excel in defining data strategies and delivering 	innovative data management and analytics solutions. My spans across process transformation, compliance solutions (AML, EMIR, GDPR), and advanced technologies like AI, Machine Learning, and Blockchain. I have successfully led digital and operational transformations, data quality remediation, and cross-functional collaborations with multicultural teams. With my own home server setup, i have various AI/ML projects live along with my personal cloud.",
                className="text-center", style={"text-align": "justify"},
            ),
            html.Div([
                html.Span([
                    html.I(className="bi bi-envelope"),  # Bootstrap icon for email
                    " sudhanshu.deo@gmail.com"
                ], className="d-block text-center"),
                html.Span([
                    html.I(className="bi bi-telephone"),  # Bootstrap icon for phone
                    " +447714419605"
                ], className="d-block text-center"),
            ], style={"marginBottom": "20px"}),
            html.Hr(),
        ], style={"marginBottom": "30px"}),

        # Bullet points section
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Ul([
                        html.Li("Bullet point 1"),
                        html.Li("Bullet point 2"),
                        html.Li("Bullet point 3"),
                    ])
                ], width=6),
                dbc.Col([
                    html.Ul([
                        html.Li("Bullet point 4"),
                        html.Li("Bullet point 5"),
                        html.Li("Bullet point 6"),
                    ])
                ], width=6),
            ])
        ]),
    ], fluid=True, id="main-content"),
    html.Div(id="theme-link"),
])

# Callback to dynamically switch theme
@app.callback(
    Output("theme-link", "children"),
    Input("theme-selector", "value"),
)
def switch_theme(selected_theme):
    return html.Link(rel="stylesheet", href=selected_theme)


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port = 8080)