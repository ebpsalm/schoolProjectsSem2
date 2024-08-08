from random import random


class Restaurant:
     separator = "*"*70
     def __init__(self):
          self.menu = [("chicken",7000),("beef",4000),("fish finger",2500),("plain pasta",3000),("cassava",3500),("ugali",4000),("biriani rice",4400),("sushi",7500),("chapati",2000),("burger",5500),("hotdog",4500),("samosa",1500),("pizza",9000),("cake",5000),("ice cream",3000),("soda",2500),("juice",3000),("water",2000),("espresso",4500),("iced coffee",5000),("redbull",3500),("beer",4000)]
          self.reserved_tables = []
          self.orders = []
     
     def addMenuItem(self, item, cost):
          self.menu.append((item,cost))
          print(f"{item} successfully added to menu.")
          return 1
     
     def placeOrder(self, order_list, table):
          order_items = []
          order_cost = 0
          for number in order_list:
               order_items.append(self.menu[number-1])
               order_cost += self.menu[number-1][1]
          current_order = {
               "number": self.getRandom(),
               "table": table,
               "order": order_items,
               "cost": order_cost
          }
          self.orders.append(current_order)
          print(f"Order {current_order['number']} has been successfully placed.")
          return 1
          
     def reserveTable(self,table,name,time_range):
          table = {
               "number": table,
               "reservation_name": name,
               "reservation_time": time_range
          }
          self.reserved_tables.append(table)
          print(f"Table {table['number']} has been reserved successfully.")
          return 1
          
     def displayMenu(self):
          print(f"\t\t\tMENU\n{self.separator}")
          item_count = 1
          for item in self.menu:
               print(f"{item_count}. {item[0].capitalize():<15} {item[1]:>10}")
               item_count += 1
          print(f"{self.separator}")
     
     def displayTableReservations(self):
          reservation_separator = '_'*50
          print(f"\t\t\tRESERVATIONS\n{self.separator}\n")
          if len(self.reserved_tables) == 0:
               print("There are currently no reservations made.")
               return
          for reservation in self.reserved_tables:
               print(f"Table Number:\t\t\t{reservation['number']}\nHolder Name:\t\t\t{reservation['reservation_name']}\nTime Range:\t\t\t{reservation['reservation_time'][0]} - {reservation['reservation_time'][1]}\n{reservation_separator}")

     def displayOrders(self):
          order_separator = '_'*50
          print(f"\t\t\tORDERS\n{self.separator}\n")
          if len(self.orders) == 0:
               print("There are currently no orders made.")
               return
          for order in self.orders:
               print(f"Order Number:\t\t\t{order['number']}\nTable Number:\t\t\t{order['table']}\nOrder cost\t\t\t{order['cost']}\nItems ordered: ", end="\t")
               for order_item in order["order"]:
                    print(f"{order_item[0]}", end="\t")
               print(f"\n{order_separator}\n")
               
     def getRandom(self):
          random_number = str(random())
          random_number = int(random_number[2:7])
          return random_number
          

