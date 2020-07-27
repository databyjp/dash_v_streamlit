# ========== (c) JP Hwang 27/7/20  ==========
def load_fig():
    import json
    import plotly.graph_objects as go
    with open("srcdata/fig.json", "r") as f:
        fig = go.Figure(json.load(f))
    return fig