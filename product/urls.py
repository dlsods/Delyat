from django.urls import path

# from product.views import products_list

# urlpatterns = [
#     # path('func/products/', products_list),
# ]


from django.urls import path

from product.views import ProductsListView, ProductDetailView, CreateProductView, UpdateProductView, \
    DeleteProductView, ProductViewSet


# view_product, update_product, product_details, create_product, delete_product, \
# patch_product


urlpatterns = [
    # path('func/', view_product),
    # path('func/<int:pk>/', product_details),
    # path('func/create/', create_product),
    # path('func/delete/<int:pk>/', delete_product),
    # path('func/update/<int:pk>/', update_product),
    # path('func/update1/<int:pk>/', patch_product),

    path('cls/products/', ProductsListView.as_view()),
    path('cls/products/<int:id>/', ProductDetailView.as_view()),
    path('cls/products/create/', CreateProductView.as_view()),
    path('cls/products/update/<int:pk>/', UpdateProductView.as_view()),
    path('cls/products/delete/<int:id>/', DeleteProductView.as_view()),

    path('set_view/products/', ProductViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('set_view/products/<int:id>/', ProductViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy'}
    )),
]
