from django.urls import path 
from .views import (index, my_tests, create_test, create_question, update_test, 
                    detail_test, update_question, ready_to_test, test, check_test,
                    my_results)


urlpatterns = [
    path("", index, name="index"),
    path("my-tests/", my_tests, name="my_tests" ),
    path("my-results/", my_results, name="my_results" ),
    path("create-test/", create_test, name="create_test"),
    path("create-question/<int:test_id>/", create_question, name="create_question"),
    path("update-test/<int:test_id>/", update_test, name="update_test"),
    path("detail-test/<int:test_id>/", detail_test, name="detail_test"),
    path("update-question/<int:question_id>/", update_question, name="update_question"),
    path("ready-to-test/<int:test_id>", ready_to_test, name="ready_to_test"),#=> endpoint
    path("test/<int:test_id>", test, name="test"),
    path("checktest/<int:checktest_id>", check_test, name="check_test"),
]
    