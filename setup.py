#!/usr/bin/env python
#
# Copyright (C) 2017 104 Corporation
# Copyright (C) 2017 Gea-Suan Lin <gslin@104.com.tw>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import find_packages, setup

PACKAGE = 'DefaultOwnerTicketPlugin'
VERSION = '0.3'

try:
    import trac
    if trac.__version__ < '1.0':
        print "%s %s requires Trac >= 1.0" % (PACKAGE, VERSION)
        sys.exit(1)
except ImportError:
    pass

setup(
    name = PACKAGE,
    version = VERSION,
    author = 'Gea-Suan Lin',
    author_email = 'gslin@104.com.tw',
    description = 'Set owner to reporter when empty',
    license = '3-Clause BSD',
    keywords = 'owner reporter trac plugin',
    packages = find_packages(),
    entry_points = {
        'trac.plugins': [
            'defaultownerticket = defaultownerticket.main',
        ],
    },
)

