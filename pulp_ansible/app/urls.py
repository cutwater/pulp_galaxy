from django.conf.urls import url

from pulp_ansible.app.galaxy.views import (
    GalaxyCollectionNamespaceNameVersionDetail,
    GalaxyCollectionNamespaceNameVersionList,
    GalaxyCollectionNamespaceNameVersionArtifactRedirect,
    GalaxyCollectionView,
    GalaxyVersionView,
    RoleList,
    RoleVersionList
)


urlpatterns = [
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/$', GalaxyVersionView.as_view()),
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/v1/roles/$', RoleList.as_view()),
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/v1/roles/(?P<role_pk>.+)/versions/$',
        RoleVersionList.as_view()),
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/v2/collections/$', GalaxyCollectionView.as_view()),
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/v2/collections/(?P<namespace>.+)/(?P<name>.+)/versions/$', GalaxyCollectionNamespaceNameVersionList.as_view()),
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/v2/collections/(?P<namespace>.+)/(?P<name>.+)/versions/(?P<version>.+)/$', GalaxyCollectionNamespaceNameVersionDetail.as_view()),
    url(r'pulp_ansible/galaxy/(?P<path>.+)/api/v2/collections/(?P<namespace>.+)/(?P<name>.+)/versions/(?P<version>.+)/artifact/$', GalaxyCollectionNamespaceNameVersionArtifactRedirect.as_view()),
]
