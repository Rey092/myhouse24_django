from django.urls import path

from . import views

app_name = "admin_panel"
urlpatterns = [
    path("", views.welcome_view, name="welcome"),
    path("statistics/", views.statistics_view, name="home"),

    path("cashbox/transactions/", views.TransactionListView.as_view(), name="transaction_list"),
    path("cashbox/transactions/create/income/", views.transaction_income_create_view, name="transaction_income_create"),
    path("cashbox/transactions/create/expense/", views.transaction_expense_create_view, name="transaction_expense_create"),
    path("cashbox/transactions/detail/<int:pk>/", views.TransactionDetailView.as_view(), name="transaction_detail"),
    path("cashbox/transactions/update/<int:pk>/", views.transaction_update_view, name="transaction_update"),
    path("cashbox/transactions/delete/<int:pk>/", views.TransactionDeleteView.as_view(), name="transaction_delete"),
    path("cashbox/transactions/xls/", views.transaction_list_xls, name="transaction_xls_list"),
    path("cashbox/transactions/xls/<int:pk>/", views.transaction_detail_xls, name="transaction_xls_detail"),

    path("receipts/", views.ReceiptListView.as_view(), name="receipt_list"),
    path("receipts/create/", views.receipt_create_view, name="receipt_create"),
    path("receipts/update/<int:pk>/", views.receipt_update_view, name="receipt_update"),
    path("receipts/delete/<int:pk>/", views.ReceiptDeleteView.as_view(), name="receipt_delete"),

    path("accounts/", views.AccountListView.as_view(), name="account_list"),
    path("accounts/create/", views.account_create_view, name="account_create"),
    path("accounts/detail/<int:pk>/", views.AccountDetailView.as_view(), name="account_detail"),
    path("accounts/update/<int:pk>/", views.account_update_view, name="account_update"),
    path("accounts/delete/<int:pk>/", views.AccountDeleteView.as_view(), name="account_delete"),
    path("accounts/xls/", views.account_xls_list, name="account_list_xls"),

    path("houses/", views.HouseListView.as_view(), name="house_list"),
    path("houses/create/", views.house_create_view, name="house_create"),
    path("houses/detail/<int:pk>/", views.HouseDetailView.as_view(), name="house_detail"),
    path("houses/update/<int:pk>/", views.house_update_view, name="house_update"),
    path("houses/delete/<int:pk>/", views.HouseDeleteView.as_view(), name="house_delete"),

    path("section/delete/", views.section_delete_view, name="section_delete"),
    path("flats/", views.FlatListView.as_view(), name="flat_list"),
    path("flats/create/", views.flat_create_view, name="flat_create"),
    path("flats/detail/<int:pk>/", views.FlatDetailView.as_view(), name="flat_detail"),
    path("flats/update/<int:pk>/", views.flat_update_view, name="flat_update"),
    path("flats/delete/<int:pk>/", views.FlatDeleteView.as_view(), name="flat_delete"),
    path("meters-data/", views.MeterDataListView.as_view(), name="meter_data_list"),
    path(
        "meters-data/by-flat/",
        views.MeterDataByFlatListView.as_view(),
        name="meter_data_list_by_flat",
    ),
    path("meters-data/create/", views.meter_data_create_view, name="meter_data_create"),
    path(
        "meters-data/delete/<int:pk>/",
        views.MeterDataDeleteView.as_view(),
        name="meter_data_delete",
    ),
    path(
        "meters-data/update/<int:pk>/",
        views.meter_data_update_view,
        name="meter_data_update",
    ),
    path("website/home/", views.site_home_view, name="site_home"),
    path("website/about/", views.site_about_view, name="site_about"),
    path("website/services/", views.site_services_view, name="site_services"),
    path("website/contacts/", views.site_contacts_view, name="site_contacts"),
    path("website/update-sitemap/", views.update_sitemap_view, name="update_sitemap"),
    path("website/delete-gallery-image/<int:pk>/", views.GalleryImageDeleteView.as_view(), name="delete_gallery_image"),
    path("website/delete-document/<int:pk>/", views.DocumentDeleteView.as_view(), name="delete_document"),
    path("website/delete-article/<int:pk>/", views.ArticleDeleteView.as_view(), name="delete_article"),

    path("api/houses/", views.api_houses, name="api_houses"),
    path("api/sections/<int:pk>/", views.api_sections, name="api_sections"),
    path("api/floors/<int:pk>/", views.api_floors, name="api_floors"),
    path("api/users/", views.api_users, name="api_users"),
    path("api/users/new/", views.api_new_users, name="api_new_users"),
    path("api/measure/", views.api_measure_name, name="api_measure_name"),
    path("api/flats/", views.api_flats, name="api_flats"),
    path("api/accounts/", views.api_accounts, name="api_accounts"),
    path("api/transaction-types/", views.api_transaction_types, name="api_transaction_types"),
    path("api/staff/", views.api_staff, name="api_staff"),
    path("api/get_owner/", views.api_get_owner, name="api_get_owner"),
    path("api/messages/delete/", views.api_delete_messages, name="api_delete_messages"),
    path("api/receipts/delete/", views.api_delete_receipts, name="api_delete_receipts"),
    path(
        "api/services/",
        views.api_get_services_from_tariff,
        name="api_get_services_from_tariff",
    ),
    path("api/meter_data/", views.api_get_meter_data, name="api_get_meter_data"),
    path("api/get_staff_role/", views.api_get_staff_role, name="api_get_staff_role"),
    path(
        "api/api_house_staff_delete/",
        views.api_house_staff_delete,
        name="api_house_staff_delete",
    ),
    path("api/master/", views.api_master, name="api_master"),
    path("api/master/types/", views.api_master_types, name="api_master_types"),
    path("api/statistics/", views.api_statistics, name="api_get_statistics"),

    path("users/", views.UserListView.as_view(), name="user_list"),
    path("users/create/", views.user_create_view, name="user_create"),
    path("users/detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("users/update/<int:pk>/", views.user_update_view, name="user_update"),
    path("users/delete/<int:pk>/", views.UserDeleteView.as_view(), name="user_delete"),

    path("system/services/", views.system_services, name="system_services"),
    path(
        "system/services/delete/measure/<int:pk>/",
        views.MeasureDeleteView.as_view(),
        name="delete_measure",
    ),
    path(
        "system/services/delete/service/<int:pk>/",
        views.ServiceDeleteView.as_view(),
        name="delete_service",
    ),
    path(
        "system/services/check/measure/<int:pk>/",
        views.check_measure,
        name="check_measure",
    ),
    path(
        "system/services/check/service/<int:pk>/",
        views.check_service,
        name="check_service",
    ),
    path(
        "system/tariffs/", views.SystemTariffsListView.as_view(), name="system_tariffs"
    ),
    path(
        "system/tariffs/create/",
        views.system_tariffs_create_view,
        name="system_tariffs_create",
    ),
    path(
        "system/tariffs/update/<int:pk>/",
        views.system_tariffs_update_view,
        name="system_tariffs_update",
    ),
    path(
        "system/tariffs/delete/<int:pk>/",
        views.TariffDeleteView.as_view(),
        name="system_tariffs_delete",
    ),
    path(
        "system/tariffs/clone/<int:pk>/",
        views.system_tariffs_clone_view,
        name="system_tariffs_clone",
    ),
    path("system/tariffs/detail/<int:pk>/", views.TariffDetailView.as_view(), name="system_tariffs_detail"),

    path("system/staff/", views.StaffListView.as_view(), name="system_staff_list"),
    path("system/staff/roles", views.system_user_role_view, name="system_staff_roles"),
    path("system/staff/create/", views.staff_create_view, name="system_staff_create"),
    path("system/staff/update/<int:pk>/", views.staff_update_view, name="system_staff_update"),
    path("system/staff/detail/<int:pk>/", views.StaffDetailView.as_view(), name="system_staff_detail"),
    path("system/staff/delete/<int:pk>/", views.StaffDeleteView.as_view(), name="system_staff_delete"),
    path("system/staff/invite/<int:pk>/", views.system_staff_invite, name="system_staff_invite"),

    path("system/credentials/", views.credentials_update_view, name="system_credentials"),
    path("system/transactions/types/", views.TransactionTypeListView.as_view(), name="system_transaction_type_list"),
    path("system/transactions/types/create/", views.transaction_type_create_view, name="system_transaction_type_create"),
    path("system/transactions/types/update/<int:pk>/", views.transaction_type_update_view, name="system_transaction_type_update"),

    path("messages/", views.MessageListView.as_view(), name="message_list"),
    path("messages/create/", views.message_create_view, name="message_create"),

    path("call-requests/", views.CallRequestListView.as_view(), name="call_request_list"),
    path("call-requests/create/", views.call_request_create_view, name="call_request_create"),
    path("call-requests/update/<int:pk>/", views.call_request_update_view, name="call_request_update"),
    path("call-requests/delete/<int:pk>/", views.CallRequestDeleteView.as_view(), name="call_request_delete"),
    path("call-requests/detail/<int:pk>/", views.CallRequestDetailView.as_view(), name="call_request_detail"),
]
