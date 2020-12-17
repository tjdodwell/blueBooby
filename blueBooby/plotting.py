import plotly.graph_objects as go
import pandas as pd
import numpy as np


class Plotting:

    def __init__(self, plane_list, inJupyter = False):

        self.aircraft = plane_list

        self.numAircraft = len(plane_list)

        self.fig = go.Figure()


    def plot(self):

        for id in range(len(self.aircraft)):

            x = self.aircraft[id].data['Lat']
            y = self.aircraft[id].data['Long']
            z = self.aircraft[id].data['Alt']
            u = self.aircraft[id].data['vx']
            v = self.aircraft[id].data['vy']
            w = self.aircraft[id].data['vz']


            self.fig.add_trace(go.Cone(x=x, y=y, z=z,u = u, v=v, w=w,
                showscale = False,
                sizemode = "scaled",
                sizeref=2
            ))



            # self.fig.add_trace(go.Scatter3d(x=x, y=y, z=z,
            #     marker=dict(
            #         size=2,
            #         color=id,
            #     ),
            #     line=dict(
            #         color=id,
            #         width=2
            #     )
            # ))

            self.fig.update_layout(
                scene = dict(
                    xaxis_title='Latitude, nm',
                    yaxis_title='Longitude, nm',
                    zaxis = dict(tick0 = 0.0, dtick = 50, range=[0,300],), zaxis_title='Flight Level',)
                )



            # Add commands

            for i in range(self.aircraft[id].commandCount):

                ts = self.aircraft[id].data['command'][i]['timestamp']

                x = [self.aircraft[id].data['Lat'][ts]]
                y = [self.aircraft[id].data['Long'][ts]]
                z = [self.aircraft[id].data['Alt'][ts]]

                self.fig.add_trace(go.Scatter3d(x=x, y=y, z=z, text = [self.aircraft[id].data['command'][i]['text']],
                    marker=dict(
                        size=6,
                        color='red',
                    )
                ))

                # self.fig.update_layout(
                #     scene=dict(
                #         annotations=[
                #         dict(
                #             showarrow=False,
                #             x=x,
                #             y=y,
                #             z=z,
                #             text="Point 1",
                #             xanchor="left",
                #             xshift=10,
                #             opacity=0.7
                #         )]
                #     ),
                # )


        self.fig.show()
