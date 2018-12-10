from django.urls import path
from banana_py.views import BananasCompleteView

urlpatterns = [
    path('bananas/ripe/', BananasCompleteView.as_view(), name='bananas_ripe'),

]
