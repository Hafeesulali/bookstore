from django.urls import path
from customer import views

urlpatterns = [

    path("home", views.CustomerIndex.as_view(), name="custhome"),
    path("accounts/register", views.SignUpView.as_view(), name="sign up"),
    path("accounts/login", views.SignInView.as_view(), name="sign in"),
    path("accounts/logout", views.signout, name="sign out"),
    path("accounts/password/reset", views.PasswordReset.as_view(), name="password reset"),
    path("carts/item/add/<int:id>",views.add_to_cart,name="addtocart"),
    path("carts/all",views.ViewMyCart.as_view(),name="viewmycart")

]
