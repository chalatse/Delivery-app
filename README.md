# Delivery-app

Method       Route                          Function                  Access
POST         /api/signup/                   Register new User         All users
POST         /api/login/                    Login User                All users
POST         /api/order/                    Place an Order            All users
PUT          /api/order/update/{order_id}/  Update an order           All users
PUT          /api/order/status/{order_id}/  Update order Status       All users
DELETE       /api/order/delete/{order_id}/  Delete an order           All users
GET          /api/user/orders/              Get users orders          All users
GET          /api/orders/                   List all the orders Made  Superuser
GET          /api/orders/{order_id}/        Retrieve an order         Superuser
GET          /api/user/order/{order_id}/    Get user's specific order Superuser
GET          /docs/                         View API Documentation    Superuser

