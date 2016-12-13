# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.constants.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Dictionary encoding.
ENCODING_DICT = "dict"

# JSON encoding.
ENCODING_JSON = "json"

# Set of supported encodings.
ENCODINGS = {
    ENCODING_DICT,
    ENCODING_JSON
}

# Governance state - the term is pending review.
GOVERNANCE_STATUS_PENDING = u'pending'

# Governance state - the term is accepted.
GOVERNANCE_STATUS_ACCEPTED = u'accepted'

# Governance state - the term is rejected.
GOVERNANCE_STATUS_REJECTED = u'rejected'

# Governance state - the term is obsolete.
GOVERNANCE_STATUS_DEPRECATED = u'obsolete'

# Set of allowed governance states.
GOVERNANCE_STATUS_SET = set([
    GOVERNANCE_STATUS_PENDING,
    GOVERNANCE_STATUS_ACCEPTED,
    GOVERNANCE_STATUS_REJECTED,
    GOVERNANCE_STATUS_DEPRECATED
])

# Regular expression for validating a canonical name.
REGEX_CANONICAL_NAME = u"/&"

# Regular expression for validating a label.
REGEX_LABEL = u"/&"

# Regular expression for validating a url.
REGEX_URL = u""
