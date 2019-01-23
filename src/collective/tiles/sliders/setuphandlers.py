# -*- coding: utf-8 -*-
"""Post install import steps for collective.tiles.sliders."""

from collective.tiles.sliders import config
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from Products.GenericSetup.interfaces import IProfileImportedEvent
from zope.component import adapter
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenMosaicProfiles(object):
    """Define hidden GS profiles."""

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            config.MOSAIC_SUPPORT_PROFILE,
            config.UNINSTALL_PROFILE,
        ]


@implementer(INonInstallable)
class HiddenTileProfiles(object):
    """Define hidden GS profiles."""

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            config.INSTALL_PROFILE,
            config.UNINSTALL_PROFILE,
        ]

def post_install(context):
    """Post install script"""


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


# @adapter(IProfileImportedEvent)
# def handle_profile_imported_event(event):
#     """Update 'last version for profile' after a full import."""
#     qi = api.portal.get_tool(name='portal_quickinstaller')
#     setup = api.portal.get_tool(name='portal_setup')

#     if not qi.isProductInstalled(config.PROJECT_NAME):
#         return

#     if event.profile_id == 'profile-plone.app.mosaic:default':
#         setup.runAllImportStepsFromProfile(config.MOSAIC_SUPPORT_PROFILE)
