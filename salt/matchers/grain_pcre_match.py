"""
This is the default grains PCRE matcher.
"""

import logging

import salt.utils.data  # pylint: disable=3rd-party-module-not-gated
from salt.defaults import (  # pylint: disable=3rd-party-module-not-gated
    DEFAULT_TARGET_DELIM,
)

log = logging.getLogger(__name__)


def match(tgt, delimiter=DEFAULT_TARGET_DELIM, opts=None, minion_id=None):
    """
    Matches a grain based on regex
    """
    if not opts:
        opts = __opts__
    log.debug("grains pcre target: %s", tgt)
    if delimiter not in tgt:
        log.error(
            "Got insufficient arguments for grains pcre match " "statement from master"
        )
        return False

    return salt.utils.data.subdict_match(
        opts["grains"], tgt, delimiter=delimiter, regex_match=True
    )
