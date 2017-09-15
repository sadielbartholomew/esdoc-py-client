"""A sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe, David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2017-08-04",
         "Initialised from CMIP5", "Charlotte Pascoe (NCAS), David Hassell (NCAS)"),
     ]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
#CMIP5_MAPPINGS_SYNCED_AT = "0.4.0"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this specialization
# --------------------------------------------------------------------
DESCRIPTION = 'Atmospheric aerosols realm'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'aerosol_grid'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties (differing from defaults (grid, timestep etc))
# --------------------------------------------------------------------
KEY_PROPERTIES = 'aerosol_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Simulated processes
# --------------------------------------------------------------------
PROCESSES = [
    'aerosol_transport',
    'aerosol_emissions_concentrations',
    'aerosol_model',
    ]