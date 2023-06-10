from django.conf.urls import url, patterns


urlpatterns = patterns(
    "",
    url(r"^$", "brabeion.views.badge_list", name="badge_list"),
    url(r"^(\w+)/(\d+)/$", "brabeion.views.badge_detail", name="badge_detail"),
)
