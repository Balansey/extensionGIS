# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Zoomer
                                 A QGIS plugin
 Zoom sur un point
                             -------------------
        begin                : 2017-11-12
        copyright            : (C) 2017 by MyCompany
        email                : rodolphe.precheur@gmail.com
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
    """Load Zoomer class from file Zoomer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Zoom import Zoomer
    return Zoomer(iface)
