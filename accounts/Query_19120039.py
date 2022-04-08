from .models import *


# Lấy hết thông tin Customer trong Table
customers = Customer.objects.all()


# Lấy thông tin Customer đầu tiên
firstCustomer = Customer.objects.first()


# Lấy thông tin Customer cuối cùng
lastCustomer = Customer.objects.last()


# Lấy thông tin, tìm kiếm Customer bằng cách truyền vào tên
customerByName = Customer.objects.get(name='Peter Piper')


# Lấy thông tin, tìm kiếm Customer bằng cách truyền vào ID
customerById = Customer.objects.get(id=4)


# Lấy hết thông tin Hoá đơn Order của Customer
firstCustomer.order_set.all()


# Tìm tên của Customer của Hoá đơn đầu tiên
order = Order.objects.first()
parentName = order.customer.name


# Lấy tất cả Product với thuộc tính là "Out Door"
products = Product.objects.filter(category="Out Door")


# Sắp xếp Product theo ID
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')


# Lấy thông tin tất cả Product có tags name là "Sports"
productsFiltered = Product.objects.filter(tags__name="Sports")


# Tính tất cả số lần sản phẩm "Ball" được đặt hàng bởi Customer đầu tiên
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()


# Tính tổng số lượng Product mỗi Order
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1


# Tạo Model Parent
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

# Tạo model CHild
class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

# Lấy thông tin tên của Model "Parent" đầu tiên trong database
parent = ParentModel.objects.first()


# Lấy tất cả tên Model "Child" mà thuộc Model "Parent" trong database
parent.childmodel_set.all()