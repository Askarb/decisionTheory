from django.conf.urls import url, include
from django.contrib import admin
import main.urls
import bond.urls
import fund.urls
import computer.urls
import food.urls
import engine.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'bond/', include(bond.urls)),
    url(r'fund/', include(fund.urls)),
    url(r'computer/', include(computer.urls)),
    url(r'food/', include(food.urls)),
    url(r'engine/', include(engine.urls)),
    url(r'', include(main.urls)),
]
