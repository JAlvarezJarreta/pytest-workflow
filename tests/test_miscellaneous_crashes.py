# Copyright (C) 2018 Leiden University Medical Center
# This file is part of pytest-workflow
#
# pytest-workflow is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# pytest-workflow is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pytest-workflow.  If not, see <https://www.gnu.org/licenses/

from .test_success_messages import SIMPLE_ECHO


def test_same_name_different_files(pytester):
    pytester.makefile(".yml", test_a=SIMPLE_ECHO)
    pytester.makefile(".yml", test_b=SIMPLE_ECHO)
    result = pytester.runpytest()
    assert result.ret != 0
    assert ("Workflow name 'simple echo' used more than once"
            in result.stdout.str())
    conflicting_message = (
        "Conflicting tests: test_b.yml::simple echo, test_a.yml::simple echo.")
    assert conflicting_message in result.stdout.str()
