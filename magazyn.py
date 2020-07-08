product1={
    "name" : ["notebook"],
    "quantity" : ["100"],
    "unit" : ["pc"],
    "unit_price" : ["3,50"]
}

product2={
    "name" : ["pen"],
    "quantity" : ["200"],
    "unit" : ["pc"],
    "unit_price" : ["2,50"]
}

product3={
    "name" : ["ink"],
    "quantity" : ["5"],
    "unit" : ["l"],
    "unit_price" : ["10"]
}

products_list=[product1, product2, product3]

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

if __name__ == "__main__":
    question= input("What would you like to do?")


if question== "exit":
    exit()
if question== "show":
    print("\n")
    print("{:>15}{:>15}{:>15}{:>15}".format("name", "quantity", "unit", "unit_price"))
    print("-"*(15*4+11))
    get_items(products_list)
if question== "add":
    new_product={}
    add1=input("name:")
    add2=input("quantity:")
    add3=input("unit:")
    add4=input("unit_price:")
    add_items(new_product)




