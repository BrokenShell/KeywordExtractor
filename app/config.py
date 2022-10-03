text_color = "#AAAAAA"
graph_color = "#333333"
graph_bg = "#252525"

configuration = dict(
    legend={
        "titleColor": text_color,
        "labelColor": text_color,
        "padding": 10,
    },
    title={
        "color": text_color,
        "fontSize": 26,
        "offset": 30,
    },
    axis={
        "titlePadding": 20,
        "titleColor": text_color,
        "labelPadding": 5,
        "labelColor": text_color,
        "gridColor": graph_color,
        "tickColor": graph_color,
        "tickSize": 10,
    },
    view={
        "stroke": graph_bg,
    },
)

properties = dict(
    width=400,
    height=420,
    padding=40,
    background=graph_bg,
)
