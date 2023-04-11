"""epicure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Homes.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



from ordering.views import mainv, orderv, paymentv, items_availv
from users.views import signupv, loginv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainv, name='Mainpage' ),
    path('order', orderv, name='Order'),
    path('payment', paymentv, name='Payment'),
    path('items_availability', items_availv, name='Items_availability'),
    path('signup', signupv, name='Signup'),
    path('login', loginv, name='Login'),
    # path('accounts/', include('accountsn.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
