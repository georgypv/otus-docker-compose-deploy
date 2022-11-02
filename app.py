import os
from time import sleep
import pandas as pd
import sqlalchemy as sa
import panel as pn
import holoviews as hv

pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_db = os.getenv("PG_DB")

hv.extension('bokeh')
pn.extension()

ROW_HEIGHT = 400

def read_db(con):
    retries = 5
    while retries > 0:
        try:
            df = pd.read_sql_table("metrics",
                                   con=con,
                                   schema="public",
                                   )
            print("Successfully read DataFrame")
            print(f"Row count is: {df.shape[0]}")
            return df
        except Exception as e:
            print("ERROR while trying to connect to DB...")
            print(str(e))
            sleep(3)
            retries -= 1
            continue
    raise Exception("Unable to connect to DB")


def plot(df):
    val_scatter = hv.Scatter(df[['val1', 'val2', 'cat']]
                             ).opts(height=ROW_HEIGHT, width=700, tools=['hover'], color='cat')
    val1_dist = hv.Distribution(df['val1']).opts(height=ROW_HEIGHT, width=500)
    val2_dist = hv.Distribution(df['val2']).opts(height=ROW_HEIGHT, width=500)
    cat_bar = hv.Bars(df.value_counts('cat').reset_index().rename(columns={0: 'count'})
                      ).opts(height=ROW_HEIGHT, width=300, tools=['hover'])

    scatter_row = pn.Row(val_scatter, cat_bar)
    dist_row = pn.Row(val1_dist, val2_dist)
    graph_container = pn.Column(scatter_row, dist_row, width_policy='max')

    return graph_container

def select_cat(cat):
    if cat == 'All':
        return plot(df)
    else:
        return plot(df[df['cat'] == cat])

con = sa.create_engine(f"postgresql://{pg_user}:{pg_password}@db:5432/{pg_db}")
df = read_db(con)

cat_selector = pn.widgets.Select(name='Select Category', default='All', options=['All', 'A', 'B', 'C'], )

layout = pn.template.BootstrapTemplate(
    title="Sample Dashboard",
)

layout.main.append(pn.bind(select_cat, cat_selector))
layout.sidebar.append(cat_selector)

layout.servable()