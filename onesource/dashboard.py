"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'onesource.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # Administration
        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=('django.contrib.auth.*',),
        ))
        
        # Jobs
        self.children.append(modules.ModelList(
            _('Jobs'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('jobs.*',),
        ))

        # Content
        self.children.append(modules.ModelList(
            _('Content'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('pages.*','journal.*','news.*','sections.models.StaffProfile',),
        ))

        # Homepage
        self.children.append(modules.ModelList(
            _('Homepage'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('sections.*',),
            exclude=('sections.models.StaffProfile',),
        ))

        # Reports
        self.children.append(modules.LinkList(
            _('Reports'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            children=[
                {
                    'title': _('Jobs'),
                    'url': '/admin/jobs/spreadsheet/',
                    'external': False,
                },
            ]
        ))

        # Link to other company pages
        self.children.append(modules.LinkList(
            _('Company'),
            column=2,
            children=[
                {
                    'title': _('Homepage'),
                    'url': 'http://www.1-sc.com/',
                    'external': True,
                },
                {
                    'title': _('Sharepoint'),
                    'url': 'https://sharepoint2.eesllc.net/',
                    'external': True,
                },
            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))


