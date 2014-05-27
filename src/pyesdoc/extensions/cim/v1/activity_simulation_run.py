"""
.. module:: activity_simulation_run.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.simulation_run document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Simulation"
    ctx.ext.type_sortkey = ctx.meta.type_sortkey = "AC"


# Set of extension functions.
EXTENDERS = (
    _set_type_display_info,
    )