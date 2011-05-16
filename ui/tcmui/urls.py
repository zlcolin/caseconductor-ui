from django.conf.urls.defaults import patterns, url, include



urlpatterns = patterns(
    "",
    url("^$", "tcmui.products.views.product_list", name="products"),
    url("^account/", include("tcmui.users.urls")),

    # run tests
    url("^environment/$",
        "tcmui.environments.views.set_environment",
        name="environment"),
    url("^product/(?P<product_id>\d+)/cycles/$",
        "tcmui.testexecution.views.cycles",
        name="cycles"),
    url("^cycle/(?P<cycle_id>\d+)/$",
        "tcmui.testexecution.views.testruns",
        name="testruns"),
    url("^run/(?P<testrun_id>\d+)/$",
        "tcmui.testexecution.views.runtests",
        name="runtests"),
    url("^result/(?P<result_id>\d+)/$",
        "tcmui.testexecution.views.result",
        name="result"),

    # manage
    url("^manage/", include("tcmui.manage.urls")),

    # results
    url("^results/", include("tcmui.results.urls")),

    # new runtest nav (wireframed)
    url(r"^wire/run/$",
        "django.views.generic.simple.direct_to_template",
        {"template": "test/wireframe.html"}),

    # a sandbox for eric to work on design ideas
    url(r"^wire/design/$",
        "django.views.generic.simple.direct_to_template",
        {"template": "design.html"}),

)
