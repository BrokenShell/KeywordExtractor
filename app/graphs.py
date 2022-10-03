from pandas import DataFrame
from altair import Chart, Theta, Color, Radius, Scale
from app.config import properties, configuration


def radial_chart(target: str, dataframe: DataFrame) -> Chart:
    base = Chart(dataframe, title=f"{target.title()} by Count").encode(
        theta=Theta("count()", stack=True),
        radius=Radius("count()", scale=Scale(type="symlog", zero=True, rangeMin=40)),
        color=Color(target, title=target.title(), legend=None),
        tooltip=[target, "count()"],
    )
    chart = base.mark_arc(innerRadius=40)
    text = base.mark_text(radiusOffset=20, size=12).encode(text="count()")
    return (chart + text).properties(**properties).configure(**configuration)
