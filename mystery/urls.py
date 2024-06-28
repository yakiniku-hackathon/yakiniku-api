from django.urls import path

from .views import (
    get_my_mysteries,
    get_mysteries,
    get_mystery,
    get_question,
    get_questions,
    get_user_mysteries_status,
    get_user_mystery_status,
    patch_mystery,
    patch_question,
    patch_user_mystery_status,
    post_mystery,
    post_question,
    post_user_mystery_status,
)

urlpatterns = [
    path("mystery", post_mystery, name="post_mystery"),
    path("mystery/", get_mysteries, name="get_mysteries"),
    path("mystery/me", get_my_mysteries, name="get_my_mysteries"),
    path("mystery/<int:mystery_id>", patch_mystery, name="patch_mystery"),
    path("mystery/<int:mystery_id>/", get_mystery, name="get_mystery"),
    path("mystery/<int:mystery_id>/question", post_question, name="post_question"),
    path("mystery/<int:mystery_id>/question/", get_questions, name="get_questions"),
    path("mystery/<int:mystery_id>/question/<int:question_id>", patch_question, name="patch_question"),
    path("mystery/<int:mystery_id>/question/<int:question_id>/", get_question, name="get_question"),
    path("mystery/status", post_user_mystery_status, name="post_user_mystery_status"),
    path("mystery/status/", get_user_mysteries_status, name="get_user_mysteries_status"),
    path("mystery/status/<int:status_id>", patch_user_mystery_status, name="patch_user_mystery_status"),
    path("mystery/status/<int:status_id>/", get_user_mystery_status, name="get_user_mystery_status"),
]
