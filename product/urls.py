from django.urls import path

from product.views import (
    product_detail_view,
    product_create_view,
    render_initail_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    product_update_view
)

app_name = "product"
urlpatterns = [
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('initial/', render_initail_data, name='product-initial'),
    path('<int:id>/update/', product_update_view, name="product-update"),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name="product-list"),
]
