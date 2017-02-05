from django.conf.urls import url, include
from django.contrib import admin
import main.urls
import bond.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'bond/', include(bond.urls)),
    url(r'', include(main.urls)),
]
