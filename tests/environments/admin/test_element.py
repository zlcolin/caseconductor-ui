# Case Conductor is a Test Case Management system.
# Copyright (C) 2011 uTest Inc.
#
# This file is part of Case Conductor.
#
# Case Conductor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Case Conductor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Case Conductor.  If not, see <http://www.gnu.org/licenses/>.
"""
Tests for Element admin.

"""
from ...admin import AdminTestCase
from ... import factories as F



class ElementAdminTest(AdminTestCase):
    app_label = "environments"
    model_name = "element"


    def test_changelist(self):
        """Element changelist page loads without error, contains name."""
        F.ElementFactory.create(name="Linux")

        self.get(self.changelist_url).mustcontain("Linux")


    def test_change_page(self):
        """Element change page loads without error, contains name."""
        e = F.ElementFactory.create(name="Linux")

        self.get(self.change_url(e)).mustcontain("Linux")