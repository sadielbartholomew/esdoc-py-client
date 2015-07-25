# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.publishing.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document publishing functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

import requests

from pyesdoc import constants
from pyesdoc import options
from pyesdoc.serialization import encode, decode
from pyesdoc.extensions import extend
from pyesdoc.utils import rt
from pyesdoc.validation import is_valid



# API url option name.
_OPT_API_URL = 'api_url'

# Publishing API endpoint.
_EP_PUBLISHING = 'publishing'

# HTTP response codes.
HTTP_RESPONSE_STATUS_200 = 200
HTTP_RESPONSE_STATUS_404 = 404
HTTP_RESPONSE_STATUS_500 = 500


def _assert_doc(doc, msg):
    """Asserts document instance.

    """
    if doc is None:
        rt.throw(msg if msg is not None else "Document instance is null.")


def _throw_invalid_doc_id():
    """Throws an error.

    """
    rt.throw("Invalid document uid (must be an instance of uuid.UUID).")


def _throw_invalid_doc_version():
    """Throws an error.

    """
    rt.throw("Invalid document version (must be either \
             'all', 'latest' or an integer.")


def _throw_connection_error():
    """Throws an error.

    """
    rt.throw("Could not connect to remote API server.")


def _throw_not_found_error():
    """Throws an error.

    """
    rt.throw("Could not find remote resource.")


def _throw_http_error():
    """Throws an error.

    """
    rt.throw("Invalid HTTP response from remote API server.")


def _throw_timeout_error():
    """Throws an error.

    """
    rt.throw("Remote API server connection timed out.")


def _throw_server_error(resp):
    """Throws an error.

    """
    rt.throw("A server side failure has occurred: {0}".format(resp.text))


def _throw_uncontrolled_server_error(resp):
    """Throws an unknown server error.

    """
    rt.throw("An uncontrolled server side failure has occurred: {0}".format(resp.text))


def _invoke_api(verb, url, data=None):
    """Invokes remote API.

    """
    headers = None if not data else {'content-type': 'application/json'}
    try:
        return verb(url, data=data, headers=headers)
    except requests.ConnectionError:
        _throw_connection_error()
    except requests.HTTPError:
        _throw_http_error()
    except requests.Timeout:
        _throw_timeout_error()


def _get_api_url(verb):
    """Helper function to return api endpoint url.

    """
    return options.get_option(_OPT_API_URL) + '/2/document/{0}'.format(verb)


def _get_doc_url(verb, uid, version, encoding=None):
    """Returns a document instance endpoint url.

    """
    url = _get_api_url(verb)
    url += "?document_id={0}&document_version={1}".format(uid, version)
    if encoding:
        url += "&encoding={0}".format(encoding)

    return url


def _parse_api_response(resp, error_on_404=True):
    """Parses response returned from API.

    """
    if resp.status_code == HTTP_RESPONSE_STATUS_404:
        if error_on_404:
            _throw_not_found_error()
    elif resp.status_code == HTTP_RESPONSE_STATUS_500:
        _throw_server_error(resp)
    elif resp.status_code != HTTP_RESPONSE_STATUS_200:
        _throw_uncontrolled_server_error(resp)


def retrieve(uid, version=constants.ESDOC_DOC_VERSION_LATEST):
    """Retrieves a document from remote repository.

    :param str|uuid.UUID uid: Document unique identifier.
    :param str|int version: Document version.

    :returns: A document from remote repository.
    :rtype: object | None

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        try:
            uid = uuid.UUID(uid)
        except ValueError:
            _throw_invalid_doc_id()
    if version != constants.ESDOC_DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _throw_invalid_doc_version()

    # Issue HTTP GET.
    url = _get_doc_url('retrieve', uid, version, constants.ESDOC_ENCODING_JSON)
    resp = _invoke_api(requests.get, url)

    # Process HTTP response.
    _parse_api_response(resp, error_on_404=False)

    # Return decoded document.
    if resp.text:
        return extend(decode(resp.json(), constants.ESDOC_ENCODING_DICT))
    else:
        return None


def publish(doc):
    """Publishes a document to remote repository.

    :param doc: Document being published.
    :type doc: object

    :returns: Updated document.
    :rtype: object

    """
    # Defensive programming.
    if doc is None:
        rt.throw("Cannot publish null documents.")
    if not is_valid(doc):
        rt.throw("Cannot publish invalid documents.")

    # Increment version.
    doc.meta.version = doc.meta.version + 1

    # Set HTTP operation parameters.
    url = _get_api_url('create')
    data = encode(doc, constants.ESDOC_ENCODING_JSON)

    # Invoke HTTP operation.
    resp = _invoke_api(requests.post, url, data)

    # Process HTTP response.
    _parse_api_response(resp)


def unpublish(uid, version=constants.ESDOC_DOC_VERSION_ALL):
    """Unpublishes a document from remote repository.

    :param str|uuid.UUID uid: Document unique identifier.
    :param str|int version: Document version.

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        try:
            uid = uuid.UUID(uid)
        except ValueError:
            _throw_invalid_doc_id()
    if not version == constants.ESDOC_DOC_VERSION_ALL and \
       not version == constants.ESDOC_DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _throw_invalid_doc_version()

    # Invoke HTTP operation.
    url = _get_doc_url('delete', uid, version)
    resp = _invoke_api(requests.delete, url)

    # Process HTTP response.
    _parse_api_response(resp)

