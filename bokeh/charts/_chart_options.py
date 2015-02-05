"""

"""
#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2014, Continuum Analytics, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from ..enums import enumeration, Orientation
from ..properties import Auto, Bool, Either, Enum, HasProps, Int, String

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

Scale = enumeration('linear', 'categorical', 'datetime')

class ChartOptions(HasProps):

    title = String(None, help="""
    A title for the chart.
    """)

    legend = Either(Bool, Enum(Orientation), help="""
    A location where the legend should draw itself.
    """)

    xgrid = Bool(True, help="""
    Whether to draw an x-grid.
    """)

    ygrid = Bool(True, help="""
    Whether to draw an x-grid.
    """)

    xlabel = String("x-axis", help="""
    A label for the (default) x-axis.
    """)

    ylabel = String("y-axis", help="""
    A label for the (default) x-axis.
    """)

    xscale = Either(Auto, Enum(Scale), help="""
    What kind of scale to use for the x-axis.
    """)

    yscale = Either(Auto, Enum(Scale), help="""
    What kind of scale to use for the x-axis.
    """)

    width = Int(600, help="""
    Width of the rendered chart, in pixels.
    """)

    height = Int(400, help="""
    Height of the rendered chart, in pixels.
    """)

    filename = Either(Bool(False), String, help="""
    A name for the file to save this chart to.
    """)

    server = Either(Bool(False), String, help="""
    A name to use to save this chart to on server.
    """)

    notebook = Either(Bool(False), String, help="""
    Whether to display the plot inline in an IPython/Jupyter
    notebook.
    """)

    tools = Bool(True, help="""
    Whether to add defaut tools the the chart.
    """)



