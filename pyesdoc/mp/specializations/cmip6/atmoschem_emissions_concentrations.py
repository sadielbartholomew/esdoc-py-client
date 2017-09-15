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
DESCRIPTION = 'Atmospheric chemistry transport'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# SUB-PROCESS: Surface emissions
# --------------------------------------------------------------------
DETAILS['surface_emissions'] = {
    'description': 'TO DO',
    'properties': [
        ('method', 'ENUM:emissions_methods', '0.N',
            'Method used to define chemical species emitted at the surface (several methods allowed because the different species may not use the same method).'),
        ('sources', 'ENUM:surface_source_types', '0.N',
             'Sources of the chemical species emitted at the surface that are taken into account in the emissions scheme'),
        ('prescribed_climatology', 'ENUM:prescribed_climatology_type', '0.1',
            'Specify the climatology type for chemical emissions prescribed at the surface'),
        ('prescribed_climatology_emitted_species', 'str', '0.1',
             'List of chemical species emitted at the surface and prescribed via a climatology'),
        ('prescribed_spatially_uniform_emitted_species', 'str', '0.1',
             'List of chemical species emitted at the surface and prescribed as spatially uniform'),
        ('interactive_emitted_species', 'str', '0.1',
             'List of chemical species emitted at the surface and specified via an interactive method'),
        ('other_emitted_species', 'str', '0.1',
             'List of chemical species emitted at the surface and specified via an "other method"'),
        ('other_method_characteristics', 'str', '0.1',
             'Characteristics of the "other method" used for chemical emissions at the surface'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Atmospheric emissions
# --------------------------------------------------------------------
DETAILS['atmospheric_emissions'] = {
    'description': 'TO DO',
    'properties': [
        ('method', 'ENUM:emissions_methods', '0.N',
            'Method used to define the chemical species emitted in the atmosphere (several methods allowed because the different species may not use the same method).'),
        ('sources', 'ENUM:atmospheric_source_types', '0.N',
             'Sources of chemical species emitted in the atmosphere that are taken into account in the emissions scheme.'),
        ('prescribed_climatology', 'ENUM:prescribed_climatology_type', '0.1',
            'Specify the climatology type for chemical emissions prescribed in the atmosphere.'),
        ('prescribed_climatology_emitted_species', 'str', '0.1',
             'List of chemical species emitted in the atmosphere and prescribed via a climatology'),
        ('prescribed_spatially_uniform_emitted_species', 'str', '0.1',
             'List of chemical species emitted in the atmosphere and prescribed as spatially uniform'),
        ('interactive_emitted_species', 'str', '0.1',
             'List of chemical species emitted in the atmosphere and specified via an interactive method'),
        ('other_emitted_species', 'str', '0.1',
             'List of chemical species emitted in the atmosphere and specified via an "other method"'),
        ('other_method_characteristics', 'str', '0.1',
             'Characteristics of the "other method" used for chemical emissions in the atmosphere'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Concentrations
# --------------------------------------------------------------------
DETAILS['concentrations'] = {
    'description': 'TO DO',
    'properties': [
        ('prescribed_lower_boundary', 'str', '0.1',
            'List of species prescribed at the lower boundary.'),
        ('prescribed_upper_boundary', 'str', '0.1',
            'List of species prescribed at the upper boundary.'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['prescribed_climatology_type'] = {
    'description': 'Specify the climatology type for chemical emissions',
    'is_open': False,
    'members': [
        ('Constant', None),
        ('Interannual', None),
        ('Annual', None),
        ('Monthly', None),
        ('Daily', None),
        ]
    }

ENUMERATIONS['surface_source_types'] = {
    'description':'Sources of the chemical species emitted at the surface that are taken into account in the emissions scheme',
    'is_open': True,
    'members':[
        ('Vegetation', None),
        ('Bare ground', None),
        ('Sea surface', None),
        ('Anthropogenic', None),
    ]
}

ENUMERATIONS['atmospheric_source_types'] = {
    'description':'Sources of the chemical species emitted in the atmosphere that are taken into account in the emissions scheme',
    'is_open': True,
    'members':[
        ('Aircraft', None),
        ('Biomass burning', None),
        ('Lightning', None),
        ('Volcanos', None),
    ]
}

ENUMERATIONS['emissions_methods'] = {
    'description': 'Method used to define chemical species emitted (several methods allowed because the different species may not use the same method).',
    'is_open': True,
    'members':[
        ('Prescribed (climatology)', None),
        ('Prescribe (spatially uniform)', None),
        ('Interactive', None),
    ]
}