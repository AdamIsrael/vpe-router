#!/usr/bin/python
##
# Copyright 2016 Canonical Ltd.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
##

from testtools import TestCase

import charmhelpers
import mock
import sys

sys.path.append('lib')
import charms.router


def patch_config(data):
    """Patch the "charmhelpers.core.hookenv.config" function.

    The mocked function returns the given value.
    """
    return mock.patch(
        'charmhelpers.core.hookenv.config',
        lambda: data)


class UnitTests(TestCase):
    """Test."""

    def setUp(self):
        """Setup."""
        super(UnitTests, self).setUp()

    @mock.patch('charms.router._run')
    def test_router_ip(self, mock_run):
        """Test that the `ip` function escapes spaces."""

        mock.return_value = True

        charms.router.ip('netns', 'add', 'network one')

        assert mock_run.called
        mock_run.assert_called_with(['ip', 'netns', 'add', "'network one'"])
