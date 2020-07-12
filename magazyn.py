product1={
    "name" : ["notebook"],
    "quantity" : [100],
    "unit" : ["pc"],
    "unit_price" : [3,50]
}

product2={
    "name" : ['pen'],
    "quantity" : [200],
    "unit" : ["pc"],
    "unit_price" : [2,50]
}

product3={
    "name" : ["ink"],
    "quantity" : [5],
    "unit" : ["l"],
    "unit_price" : [10]
}

products_list=[product1, product2, product3]
sold_items=[]



def get_items(products_list):
    for product in products_list:
        for key, value in product.items():
            result= print("{:>15}".format(*product[key]), end="")
        print("\n")
    return result

def add_items(new_product):
    new_product={
        "name" : [add1],
        "quantity" : [add2],
        "unit" : [add3],
        "unit_price" : [add4]
    }
    result=products_list.append(new_product)
    return result



def sell_items(sold_product):
    sold_product={
        "name": [sell1],
        "quantity" : [sell2]
    }
    for product in products_list:
        if product["name"]== sold_product["name"]:
            old_quantity= product['quantity']
            new_quantity=[old - sell2 for old in old_quantity]
            product['quantity']= new_quantity
            sold_product["unit"]=product["unit"]
            sold_product["unit_price"]=product["unit_price"]
            result=sold_items.append(sold_product)
            return result


        else:
            continue

def get_costs(products_list):
    result= sum([product["quantity"][0] * product["unit_price"][0] for product in products_list])
    return result

def get_income(sold_items):
    result= sum([product["quantity"][0] * product["unit_price"][0] for product in sold_items])
    return result
        
                   
    


    

if __name__ == "__main__":
    while True:
        question= input("What would you like to do?")


        if question== "exit":
            break
        if question== "show":
            print("\n")
            print("{:>15}{:>15}{:>15}{:>15}".format("name", "quantity", "unit", "unit_price"))
            print("-"*(15*4+11))
            get_items(products_list)
        if question== "add":
            print("Adding to warehouse...")
            new_product={}
            add1=input("name:")
            add2=input("quantity:")
            add3=input("unit:")
            add4=input("unit_price:")
            add_items(new_product)
            print("Succesfully added to warehouse")
            print("\n")
            print("{:>15}{:>15}{:>15}{:>15}".format("name", "quantity", "unit", "unit_price"))
            print("-"*(15*4+11))
            get_items(products_list)

        if question == "sell":
            sold_product={}
            sell1=input("Item name: ")
            sell2=int(input("Quantity to sell: "))
            sell_items(sold_product)
            print("Succesfully sold " + str(sell2) + " of " + sell1)
            print("\n")
            print("{:>15}{:>15}{:>15}{:>15}".format("name", "quantity", "unit", "unit_price"))
            print("-"*(15*4+11))
            get_items(products_list)
            print(sold_items)
        
        if question == "show_revenue":
            income=get_income(sold_items)
            cost=get_costs(products_list)
            print("Revenue breakdown (PLN)")
            print("Income: ", income)
            print("Costs: ", cost)
            print("------------")
            print("Revenue: ", income - cost)
            





