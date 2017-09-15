"""A process specialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe, David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Aerosol transport'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level aerosol transport properties',
    'properties': [
        ('scheme', 'ENUM:transport_schemes', '1.1',
            'Method for aerosol transport modeling'),
        ('mass_conservation_scheme', 'ENUM:mass_conservation_methods', '1.N',
            'Method used to ensure mass conservation.'),
        ('convention_scheme', 'ENUM:convection_types', '1.N',
            'Transport by convention'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Turbulence
# --------------------------------------------------------------------
DETAILS['turbulence'] = {
    'description': 'The scheme used for parametrization of the turbulent transport of aerosols',
    'properties': [
        ('method', 'ENUM:turbulence_methods', '1.1',
            'Method used for turbulence parametrization'),
        ('specific_scheme', 'str', '0.1',
             'Description of the scheme used for parametrization of the turbulent transport of aerosols, if not that used by the atmospheric chemistry model'),        
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['transport_schemes'] = {
    'description': 'Method for aerosol transport modeling',
    'is_open': False,
    'members': [
        ('Uses Atmospheric chemistry transport scheme', None),
        ('Specific transport scheme (eulerian)', None),
        ('Specific transport scheme (semi-lagrangian)', None),
        ('Specific transport scheme (eulerian and semi-lagrangian)', None),
        ('Specific transport scheme (lagrangian)', None),
    ]
}

ENUMERATIONS['mass_conservation_methods'] = {
    'description':'Method used to ensure mass conservation',
    'is_open': True,
    'members':[
        ('Uses Atmospheric chemistry transport scheme', None),
        ('Mass adjustment', None),
        ('Concentrations positivity', None),
        ('Gradients monotonicity', None),
    ]
}

ENUMERATIONS['convection_types'] = {
    'description':'Transport by convection',
    'is_open': True,
    'members':[
        ('Uses Atmospheric chemistry transport scheme', None),
        ('Convective fluxes connected to tracers', None),
        ('Vertical velocities connected to tracers', None),
    ]
}

ENUMERATIONS['turbulence_methods'] = {
    'description':'Method used for turbulence parametrization',
    'is_open': True,
    'members':[
        ('Uses Atmospheric chemistry turbulence scheme', None),
        ('Specific turbulence scheme', None),
    ]
}