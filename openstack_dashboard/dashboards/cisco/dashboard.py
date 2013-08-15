# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Cisco Systems, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Abishek Subramanian, Cisco Systems, Inc.

from django.utils.translation import ugettext_lazy as _
from openstack_dashboard.api import neutron as neutron

import horizon


#class PlatPanels(horizon.PanelGroup):
#    slug = "cisco"
#    name = _("Nexus Platform")
#    panels = ('nexus1000v')


class Cisco(horizon.Dashboard):
    name = _("Cisco")
    slug = "cisco"
    panels = ('nexus1000v',)  # Add your panels here.
    default_panel = 'nexus1000v'  # Specify the slug of the dashboard's default panel.
    permissions = ('openstack.roles.admin',)


if (neutron.CISCO_N1K == True):
    horizon.register(Cisco)
