from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('new', views.new_note),
    path('see', views.see_completed),
    path('see_active_notes', views.see_active),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
    path('<int:pk>/complete', views.complete, name='note-complete'),
]