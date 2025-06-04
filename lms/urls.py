from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("auth/signup", views.signup),
    path("auth/login", views.login_view),
    path("auth/me", views.me),
    path("auth/settings", views.settings),

    path("students/", views.students_collection),
    path("students/<int:id>", views.student_detail),

    path("curriculum/", views.curriculum_collection),
    path("curriculum/<int:student_id>", views.curriculum_by_student),
    path("curriculum/detail/<int:id>", views.curriculum_detail),
    path("progress/<int:id>", views.progress_update),

    path("session/record", views.session_record),
    path("session/calendar", views.session_calendar),

    path("invoice/preview", views.invoice_preview),
    path("invoice/send", views.invoice_send),
    path("invoice/history", views.invoice_history),
    path("invoice/<int:id>", views.invoice_update),

    path("report/generate", views.report_generate),
    path("report/<int:id>", views.report_update),
    path("report/send", views.report_send),
    path("report/history", views.report_history),

    path("notifications/todo", views.notifications_todo),
]
