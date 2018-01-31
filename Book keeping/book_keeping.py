import datetime

class Product:
	def __init__(self, name):
		self.name = name

# mfg = manufacturing date
# bbd = best before date	   
class Batch:
	def __init__(self, id_batch, product_name, batch_number, mfg, bbd, quantity):
		self.id_batch = id_batch
		self.product_name = product_name
		self.batch_number = batch_number
		self.mfg = mfg
		self.bbd = bbd
		self.quantity = quantity
			
	def bbd_as_date(self):
		date_bbd = datetime.datetime.strptime(self.bbd, '%d.%m.%Y').date()
		return date_bbd
		
	def __repr__(self):
		return repr((self.id_batch, self.product_name, self.batch_number, self.mfg, self.bbd, self.quantity))

class Warehouse:
	def __init__(self):
		self.products = []
		self.batches = []
	
	def add_product(self, product_name):
		self.products.append(product_name)

	def add_batch(self, batch):
		self.batches.append(batch)
		
	def batches_of_product(self, product_name):
		product_batches = []
		for batch in self.batches:
			if product_name == batch.product_name:
				product_batches.append(batch)
		return product_batches
	
	def all_batches(self):
		return self.batches
	
	def batches_sorted_by_bbd(self, product_name): 
		sorted_bbd = sorted(self.batches_of_product(product_name), key = lambda x: x.bbd_as_date(), reverse = False)
		return sorted_bbd
		
	def remove_quantity_fifo(self, product_name, desired_quantity):
		if desired_quantity <= 0:
			raise RuntimeError ('Please choose a positive quantity')
		
		if product_name not in self.products:
			raise RuntimeError ('The product does not exist in your warehouse')
		
		i = 0
		removed_quantity = 0
		while desired_quantity > 0 and i < len(self.batches):
			if self.batches[i].product_name == product_name and self.batches[i].quantity> 0 and self.batches[i].quantity < desired_quantity:
				desired_quantity = desired_quantity - self.batches[i].quantity
				removed_quantity += self.batches[i].quantity
				self.batches[i].quantity = 0
				i = i + 1
			elif self.batches[i].product_name == product_name and self.batches[i].quantity> 0 and self.batches[i].quantity > desired_quantity:
				self.batches[i].quantity = self.batches[i].quantity - desired_quantity
				removed_quantity += desired_quantity
				desired_quantity = 0
		return removed_quantity
		
	#returns the removed quantity  
	#which may be less than the desired_quantity
	def remove_quantity_fefo(self, product_name, desired_quantity):
		if desired_quantity <= 0:
			raise RuntimeError ('Please choose a positive quantity')
		
		if product_name not in self.products:
			raise RuntimeError ('The product does not exist in your warehouse')
		
		sorted_batches = self.batches_sorted_by_bbd(product_name)
		i = 0 
		removed_quantity = 0
		while desired_quantity > 0 and i < len(sorted_batches):
			if sorted_batches[i].quantity> 0 and sorted_batches[i].quantity < desired_quantity:
				desired_quantity = desired_quantity - sorted_batches[i].quantity
				removed_quantity += sorted_batches[i].quantity
				sorted_batches[i].quantity = 0
				i = i + 1
			elif sorted_batches[i].quantity> 0 and sorted_batches[i].quantity > desired_quantity:
				sorted_batches[i].quantity = sorted_batches[i].quantity - desired_quantity
				removed_quantity += desired_quantity
				desired_quantity = 0
		return removed_quantity
					
			
#warehouse = Warehouse()
#tertensif = Product('Tertensif')
#nifedipin = Product('Nifedipin')
#warehouse.add_product('Tertensif')
#warehouse.add_product('Nifedipin')
#batch_321234 = Batch(1, 'Tertensif', '321234', '23.04.2017', '30.04.2020', 100)
#batch_321235 = Batch(2, 'Tertensif', '321235', '13.10.2016', '31.10.2019', 200)
#batch_321236 = Batch(3, 'Tertensif', '321236', '20.01.2017', '30.01.2020', 500)
#batch_1010 = Batch(4, 'Nifedipin', '1010', '04.03.2014', '31.03.2018', 30)
#batch_1011 = Batch(5, 'Nifedipin', '1011', '05.10.2015', '31.10.2019', 57)
#batch_1012 = Batch(6, 'Nifedipin', '1012', '20.12.2016', '31.12.2020', 200)
#warehouse.add_batch(batch_321234)
#warehouse.add_batch(batch_321235)
#warehouse.add_batch(batch_321236)
#warehouse.add_batch(batch_1010)
#warehouse.add_batch(batch_1011)
#warehouse.add_batch(batch_1012)

# print warehouse.batches_of_product('Tertensif')
# print warehouse.batches_sorted_by_bbd('Tertensif')

#print warehouse.remove_quantity_fefo('Tertensif', 10)
#print warehouse.remove_quantity_fifo('Tertensif', 400)
#print warehouse.all_batches()
