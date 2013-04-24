"""
.. module:: cim.v1_5.types.activity.experiment_relationship_target.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.655742.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.activity.numerical_experiment import NumericalExperiment
from pyesdoc.ontologies.cim.v1_5.types.shared.cim_reference import CimReference


class ExperimentRelationshipTarget(object):
    """A concrete class within the cim v1.5 type system.

    
    """

    def __init__(self):
        """Constructor"""
        super(ExperimentRelationshipTarget, self).__init__()
        self.numerical_experiment = None             # type = activity.NumericalExperiment
        self.reference = None                        # type = shared.CimReference


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'numerical_experiment', self.numerical_experiment, False, False, False)
        append(d, 'reference', self.reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

