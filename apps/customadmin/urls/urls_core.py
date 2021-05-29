from django.urls import path
from . import views

app_name='customadmin'

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
        # User
    path("users/", views.UserListView.as_view(), name="user-detail"),

    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="user-detailview"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("users/<int:pk>/password/", views.UserPasswordView.as_view(), name="user-password"),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),

    path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]

urlpatterns +=[
#------------------------------------------------------------------------------------------------------
    #Plan
    path("plans/<int:pk>/detail/", views.PlanDetailView.as_view(), name="plan-detailview"),

    path("plans/", views.PlanListView.as_view(), name="plan-detail"),
    path("plans/", views.PlanListView.as_view(), name="plan-list"),
    path("plans/create/", views.PlanCreateView.as_view(), name="plan-create"),
    path("plans/<int:pk>/update/", views.PlanUpdateView.as_view(), name="plan-update"),
    path("plans/<int:pk>/delete/", views.PlanDeleteView.as_view(), name="plan-delete"),
    path("ajax-plans", views.PlanAjaxPagination.as_view(), name="plan-list-ajax"),
#------------------------------------------------------------------------------------------------------

]