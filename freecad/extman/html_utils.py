# -*- coding: utf-8 -*-
# ***************************************************************************
# *                                                                         *
# *  Copyright (c) 2020 Frank Martinez <mnesarco at gmail.com>              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *  This program is distributed in the hope that it will be useful,        *
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of         *
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
# *  GNU General Public License for more details.                           *
# *                                                                         *
# *  You should have received a copy of the GNU General Public License      *
# *  along with this program.  If not, see <https://www.gnu.org/licenses/>. *
# *                                                                         *
# ***************************************************************************

import os

from freecad.extman import get_resource_path, isWindowsPlatform


class Components:
    def __init__(self, **comps):
        for k, v in comps.items():
            setattr(self, k, v)


def get_resource_url(*path):
    """
    Translate path into (url, parent_url, abs_path)
    """

    file_path = get_resource_path('html', *path)
    parent = os.path.dirname(file_path)
    if isWindowsPlatform:
        url = file_path.replace('\\', '/')
        parent_url = parent.replace('\\', '/')
    else:
        url = file_path
        parent_url = parent
    return "file://" + url, "file://" + parent_url, file_path
