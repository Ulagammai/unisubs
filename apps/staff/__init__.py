# Amara, universalsubtitles.org
#
# Copyright (C) 2016 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# http://www.gnu.org/licenses/agpl-3.0.html.

"""
The staff app manages the staff section of the site.  This section contains
staff-only pages to manage things that work on a higher-level than the django
admin.

Staff pages aren't auto-generated like the django admin pages.  All the staff
app does is serve up an index page that links to pages created by other apps.
"""

import collections

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

StaffLink = collections.namedtuple('StaffLink', 'section title index_view')

all_links = []

def register(section, title, index_view):
    all_links.append(StaffLink(section, title, index_view))

def get_sections():
    sections = collections.defaultdict(list)
    for link in all_links:
        section = unicode(link.section)
        sections[section].append((link.title, reverse(link.index_view)))
    rv = sections.items()
    rv.sort()
    for section, links in rv:
        links.sort()
    return rv
