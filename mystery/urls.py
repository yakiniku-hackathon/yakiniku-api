from django.urls import path

from .views import get_mysteries, get_mystery, get_question, get_questions, patch_mystery, patch_question, post_mystery, post_question

urlpatterns = [
    path("mystery", post_mystery, name="post_mystery"),
    path("mystery/", get_mysteries, name="get_mysteries"),
    path("mystery/<int:mystery_id>", patch_mystery, name="patch_mystery"),
    path("mystery/<int:mystery_id>/", get_mystery, name="get_mystery"),
    path("mystery/<int:mystery_id>/question", post_question, name="post_question"),
    path("mystery/<int:mystery_id>/question/", get_questions, name="get_questions"),
    path("mystery/<int:mystery_id>/question/<int:question_id>", patch_question, name="patch_question"),
    path("mystery/<int:mystery_id>/question/<int:question_id>/", get_question, name="get_question"),
]
