from django.conf.urls import url

from . import views

urlpatterns = (
    url(
        r'^$',
        views.dashboard,
        name='dashboard',
    ),
    url(
        r'^access_requests/$',
        views.access_request_list,
        name='secrets.access_request-list',
    ),
    url(
        r'^access_requests/(?P<hashid>\w+)$',
        views.access_request_detail,
        name='secrets.access_request-detail',
    ),
    url(
        r'^access_requests/(?P<hashid>\w+)/(?P<action>(allow|deny))$',
        views.access_request_review,
        name='secrets.access_request-review',
    ),
    url(
        r'^opensearch.xml$',
        views.opensearch,
        name='opensearch',
    ),
    url(
        r'^secrets/$',
        views.secret_list,
        name='secrets.secret-list',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)$',
        views.secret_detail,
        name='secrets.secret-detail',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/delete$',
        views.secret_delete,
        name='secrets.secret-delete',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/download$',
        views.secret_download,
        name='secrets.secret-download',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/edit$',
        views.secret_edit,
        name='secrets.secret-edit',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/request_access$',
        views.access_request_create,
        name='secrets.secret-request_access',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/restore$',
        views.secret_restore,
        name='secrets.secret-restore',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/share$',
        views.secret_share,
        name='secrets.secret-share',
    ),
    url(
        r'^secrets/add/(?P<content_type>\w+)$',
        views.secret_add,
        name='secrets.secret-add',
    ),
    url(
        r'^secrets/live-search$',
        views.secret_search,
        name='secrets.secret-search',
    ),
)
