from django.urls import path

from .views import (
    index,
    other_page,
    BBLoginView,
    profile,
    BBLogoutView,
    ChangeUserInfoView,
    BBPasswordChangeView,
    RegisterUserView,
    RegisterDoneView,
    user_activate,
    DeleteUserView,
    by_rubric,
    detail,
    # profile_bb_detail
)

app_name = 'main'

urlpatterns = [
    path(
        'accounts/register/activate/<str:sign>/',
        user_activate,
        name='register_activate'
    ),
    path(
        'accounts/register/done/',
        RegisterDoneView.as_view(),
        name='register_done'
    ),
    path(
        'account/register',
        RegisterUserView.as_view(),
        name='register'
    ),
    path(
        'accounts/logout/',
        BBLogoutView.as_view(),
        name='logout'
    ),
    path(
        'accounts/password/change/',
        BBPasswordChangeView.as_view(),
        name='password_change.html'
    ),
    path(
        'accounts/profile/change/',
        ChangeUserInfoView.as_view(),
        name='profile_change'
    ),
    path(
        'accounts/profile/dlete',
        DeleteUserView.as_view(),
        name='profile_delete'
    ),
    path(
        'accounts/profile/',
        profile,
        name='profile'
    ),
    path(
        'accounts/login/',
        BBLoginView.as_view(),
        name='login'
    ),
    path(
        '<int:rubric_pk>/<int:pk>',
        detail,
        name='detail'
    ),
    path(
        '<int:pk>/',
        by_rubric,
        name='by_rubric'
    ),
    path(
        '<str:page>/',
        other_page,
        name='other'
    ),
    path(
        '',
        index,
        name='index'
    ),
]
