#!/usr/bin/env python
#
# Copyright (C) 2017 104 Corporation
# Copyright (C) 2017 Gea-Suan Lin <gslin@104.com.tw>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator

class DefaultOwnerTicket(Component):
    implements(ITicketManipulator)

    def prepare_ticket(self, req, ticket, fields, actions):
        pass

    def validate_ticket(self, req, ticket):
        if 'preview' in req.args:
            return []

        if not ticket.values.get('owner'):
            ticket['owner'] = ticket['reporter']

        return []
