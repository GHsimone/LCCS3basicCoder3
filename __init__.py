# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LCCS3_BasicCoder_3
                                 A QGIS plugin
 The plugin loads a LCCS3 legend, creates a form with all LCCS3 classes and allows the user to code selected features
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-09-13
        copyright            : (C) 2018 by Simone Maffei
        email                : simone.maffei@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LCCS3_BasicCoder_3 class from file LCCS3_BasicCoder_3.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .lccs3_basiccoder_3 import LCCS3_BasicCoder_3
    return LCCS3_BasicCoder_3(iface)
