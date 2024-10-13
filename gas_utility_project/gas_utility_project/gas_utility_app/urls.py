from django.urls import path
from gas_utility_app.views import customer_views, support_views  # Corrected imports

urlpatterns = [
    path('', customer_views.homepage, name='homepage'),
    path('submit-request/', customer_views.submit_request, name='submit_request'),
    path('track-request/<int:request_id>/', customer_views.track_request, name='track_request'),
    path('requests/', support_views.list_requests, name='request_list'),
    path('resolve-request/<int:request_id>/', support_views.resolve_request, name='resolve_request'),
]


