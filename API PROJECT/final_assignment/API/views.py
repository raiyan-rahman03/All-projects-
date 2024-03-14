from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django.contrib.auth.models import Group, User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import HttpResponse

# upre gula important import
# catagory list er api class eta

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# menuitem er api jetate manager only kaj korte parbe maneh notun menu item add korbe

class Manager_menuItems(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields=['title']
# menuitem er api jetate manager only kaj korte parbe maneh menu item update and delete korbe

class Manager_menuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields=['title']

'''ei nicher func ta mainly use kora jate single endpoint use kore alada
 functionality use kora jai jemon manager jokhon user hobe tokhon she add dlt upd etc 
 korte parbe and user mean customer jokhon dhukbe tokhon only menu items dekhte parbe 
 kisu korte parbena  
'''
@csrf_exempt  # eita use korte hoi jate auth error na khai dev environment eh
# eita check korbe request taki authenticated kina
@permission_classes([IsAuthenticated])
# pk none set kora karon jate pk jdi na dei tau run korte pare code
def menu_items_view(request, pk=None):
    manager_group_name = 'Manager'  # eita group er name set kora
# checking if the request is from the manager
    # 1st check je jdi manager hoi
    if request.user.groups.filter(name=manager_group_name).exists():
        if pk is None:  # eita check korbe je user request ki shob menutitem chaise kina
            # then taile oi menuitem class ta retun korbe
            return Manager_menuItems.as_view()(request)
        if pk is not None:  # eita check korbe je user single menu item chaise kina
            # jdi user er url parameter eh pk thake taile oi pk ta func er psrsmeter pk te assign hobe and pk onujai data fetch korbe
            return Manager_menuItem.as_view()(request, pk=pk)

    else:  # same above just eita normal customer er jonno
        if pk is None:
            return all_menu_items(request)
        if pk is not None:
            return single_menu_item(request, pk=pk)

# for normal staff user or customer to get all menu
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_menu_items(request):
    if request.method == 'GET':
        data = MenuItem.objects.all()
        serializer = MenuItemSerializer(data, many=True)
        return Response(serializer.data)
    else:
        return Response(status=403)

# for normal staff user or customer to get single menu

@api_view(['GET'])
def single_menu_item(request, pk):
    if request.method == 'GET':
        try:
            data = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(data)
            return Response(serializer.data)
        except MenuItem.DoesNotExist:
            return Response(status=404)
    else:
        return Response(status=403)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def group_org(request, name):
    # check korbe je manager request korse kina
    if request.user.groups.filter(name="Manager").exists():
        if request.method == "GET":
            try:
                # name onujai grp assign hobe variable eh
                group = Group.objects.get(name=name)
                # assigned grp theke user jei foreign instance ase oita dibe and all er karone shob user dibe
                users = group.user_set.all()
                # then oi user data ta serialize hobe anf many field tai maney=true
                serializer = UserSerializer(users, many=True)
                # then serialze kora data ta dibe
                return Response(serializer.data)
            except Group.DoesNotExist:
                return Response({"detail": f"Group with name '{name}' does not exist."}, status=404)

        if request.method == "POST":
            # first eh request header jei token ta ase oi ta nibe
            user_token = request.data.get('token')
            try:
                token_obj = Token.objects.get(
                    key=user_token)  # then oi token ta milabe
                user = token_obj.user  # tarpor oi token ta jar sheiti user eh assign hoye jabe
                # jei grp eh dhukate hobe setar name nilo
                target_group = Group.objects.get(name=name)
                # then oi token dara assign user ta grp eh chole gelo
                user.groups.add(target_group)
                return Response({"detail": f"User '{user.username}' added to group '{name}'."}, status=201)

            except Token.DoesNotExist:
                return Response({"detail": "Invalid token."}, status=404)
            except Group.DoesNotExist:
                return Response({"detail": f"Group with name '{name}' does not exist."}, status=404)

    else:
        return Response({"detail": "Permission denied."}, status=403)

@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_grp_user(request, id, name):
    # user ta assign korlo url eh pauwa id diye
    user = get_object_or_404(User, pk=id)
    group = get_object_or_404(Group, name=name)

    try:
        user.groups.remove(group)
        return Response({"detail": f"User with id {id} removed from group {name} successfully."})
    except:
        return Response({"detail": f"Failed to remove user with id {id} from group {name}."}, status=400)

class CartView(generics.ListAPIView):
    serializer_class = cart_get

    def get_queryset(self):
        # Filter the queryset based on the current user
        return Card.objects.filter(user=self.request.user)

class CartAddView(generics.CreateAPIView):
    serializer_class = cart_add

    def perform_create(self, serializer):
        existing_cart_item = Card.objects.filter(user=self.request.user)

        if existing_cart_item.exists():
            return Response({"detail": "You already have a cart. Delete it before adding a new one."}, status=403)

        # If the user doesn't have a cart item, create a new one
        serializer.save(user=self.request.user)
        return Response({"detail": "Cart item created successfully."})

class cart_del(generics.RetrieveDestroyAPIView):
    serializer_class = cart_get

    def get_object(self):
        # Retrieve the cart associated with the authenticated user
        return generics.get_object_or_404(Card, user=self.request.user)

    def perform_destroy(self, queryset):

        # Delete the cart instance
        queryset.delete()

@permission_classes([IsAuthenticated])
class oder_view(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name="Manager").exists():

            return Order.objects.all()
        elif self.request.user.groups.filter(name="delivery").exists():
            return Order.objects.filter(delivery_crew=self.request.user)
        else:
            return Order.objects.filter(user=self.request.user)

# eita thik hoisilo
class oder_view_post(generics.CreateAPIView):
    ''' eita user er  order post kore hoise 

      '''
    serializer_class = Order_post

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        user_card = get_object_or_404(Card, user=user)
        total = user_card.price

        # Save the Order object first to get its ID
        order = serializer.save(user=user, total=total)

        # Automatically create OrderItem objects for each item in the user's card

        OrderItem.objects.create(
            order=order,  # Use the newly created Order object
            menu_item=user_card.menu_item,
            quantity=user_card.quantity,
            unit_price=user_card.quantity_price,
            price=user_card.price
        )

        user_card.delete()
        # eitar kaj baki ase eita order dei and orderitems create kore and delete kore


class user_order(generics.ListAPIView):  # user er order item show kore
    serializer_class = orderitem_post

    def get_queryset(self):
        # Assuming you want to get all order items related to the user's orders

        if self.request.user.groups.filter(name="Manager").exists():
            return OrderItem.objects.all()
        elif self.request.user.groups.filter(name="delivery").exists():
            order_for_delivery = Order.objects.filter(
                delivery_crew=self.request.user)
            return OrderItem.filter(order__in=order_for_delivery)
        else:
            user_orders = Order.objects.filter(user=self.request.user)
            return OrderItem.objects.filter(order__in=user_orders)
'''
order__in=user_orders: This filter is applied to the OrderItem model, and it means "give me all OrderItem instances 
where the order field is in the list of orders specified by user_orders." It's a way to filter OrderItem instances
based on a relationship with the related Order model.
'''

# order
class manager_order_up_and_dev(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()  # Set the default queryset
    # Set the default serializer class

    def get_queryset(self):
        if self.request.user.groups.filter(name="Manager").exists():
            return Order.objects.all()  # Managers can view all orders
        elif self.request.user.groups.filter(name="delivery").exists():
            # Delivery users can view their assigned orders
            return Order.objects.filter(delivery_crew=self.request.user)
        return Order.objects.none()  # Other users cannot view any orders

    def delete(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name="Manager").exists():
            return Response({"error": "Only managers can delete orders."}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.user.groups.filter(name="delivery").exists():
            return delivery  # Use DeliverySerializer for delivery users
        if self.request.user.groups.filter(name="Manager").exists():
            return OrderSerializer
