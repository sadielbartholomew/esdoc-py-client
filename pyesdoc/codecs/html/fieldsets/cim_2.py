# -*- coding: utf-8 -*-

"""
.. module:: cim_1.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.html.fieldsets.field_info import FieldInfo
from pyesdoc.ontologies import cim



# Document field sets.
FIELDSETS = {
    'cim.2.designing.numericalexperiment-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: " | ".join(v)),
        FieldInfo('Related Experiments',
                  link_factory=lambda exp: [(i.name, i.viewer_url) for i in \
                                            sorted(exp.related_experiments_references, key=lambda v: v.name)])
    ],

    str(cim.v2.designing.EnsembleRequirement) : [
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Ensemble Type', path='ensemble_type'),
        FieldInfo('Minimum Size', path='minimum_size'),
        FieldInfo('Conformance Requested ?', path='conformance_is_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: " | ".join(v))
    ],

    str(cim.v2.designing.ForcingConstraint) : [
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Forcing Type', path='forcing_type'),
        FieldInfo('Conformance Requested ?', path='conformance_is_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: " | ".join(v))
    ],

    str(cim.v2.designing.TemporalConstraint) : [
        FieldInfo('Start Date', path='start_date.value'),
        FieldInfo('Required Duration', path='required_duration',
          input_formatter=lambda v: "{} {}".format(v.length, v.units)),
        FieldInfo('Description', path='description'),
        FieldInfo('Conformance Requested ?', path='conformance_is_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: " | ".join(v))
    ],

    'cim.2.shared.citation' : [
        FieldInfo('Long Title', path='citation_str', link_path="url.linkage"),
        FieldInfo('Context', path='context'),
        FieldInfo('DOI', path='doi', link_path=lambda v: "https://doi.org/{}".format(v.doi)),
        FieldInfo('Abstract', path='abstract'),
    ],

    'cim.2.shared.party' : [
        FieldInfo('Name', path='name', link_path="url.linkage"),
        FieldInfo('Address', path='address'),
        FieldInfo('Email', path='email', email_path='email'),

    ]
}
