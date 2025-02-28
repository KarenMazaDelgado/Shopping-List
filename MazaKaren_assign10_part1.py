'''
Karen Maza
'''

#used to find product with the longest name in inventory to format a table of all products
longestItem = 0

# function:   validate
# input:      (1) a string to prompt the user with ('Enter a number: ')
#             (2) a data type (string) - either 'float' or 'integer'
#                 default this value to 'float' if none is supplied
#             (3) the lowest possible number you can accept as part of
#                 your validation (integer) - default to the string "unlimited"
#                 if no integer is provided
#             (4) the highest possible number you can accept as part of
#                 your validation (integer) - default to the string "unlimited"
#                 if no integer is provided
#
#             note: you can tell Python to assign a 'default' value to an argument
#             by using this syntax in your function definition:
#
#             def foo(a, b, c="hello", d=57)
#
#             in this case 'a' and 'b' are required arguments and must be supplied
#             'c' and 'd' are optional, and if they are not supplied they will be
#             assigned the values 'hello' and 57 respectively.  for example:
#
#             foo(10, 20) # function receives a=10 b=20 c="hello" d=57
#             foo(10, 20, 30)  # function receives a=10, b=20 c=30, d=57
#             foo(10, 20, 30, 40)  # function receives a=10, b=20 c=30 d=40
#
# processing: continually prompts the user with the prompt provided. the user's
#             input will be converted to the data type requested.  if the data type
#             conversion results in a runtime error the program should not crash but
#             but alert the user with a print statement (i.e. Not a number, try again")
#             if the result is successful the function will ensure that it falls within
#             the bounds provided.
# output:     returns the validated user input (float or int)
def validate(prompt, datatype="float", low="unlimited", high="unlimited"):
    while True:
        try:
            #converts inputted number into a float or int depending on datatype supplied
            request = input(prompt)
            if datatype == 'integer':
                request = int(request)
            else:
                request = float(request)
        except:
            #makes sure input is a number
            print("Not a number, try again")
        else:
            try:
                #makes sure number supplied is in the correct range, if specified
                if request > low and request <= high:
                    return request
            except:
                #runs if no range is supplied (compares integer with string, produces error)
                return request
            else:
                print("Invalid range, try again")


inventory = {
                'soft drink': [0.99, 10],
                'onion rings': [1.29, 5],
                'small fries': [1.49, 20]
            }


while True:
    #counter helps determine if an inputted product is found in list of products, needs to be in while loop to reset counter after each iteration
    found = 0
    
    command = input("(s)earch,(l)ist,(a)dd,(r)emove,(u)pdate, r(e)port or (q)uit: ")
    command = command.lower()
    print()
    #program will end if user enters q
    if command == "q":
        print("See you soon!")
        break
    #searches for product name
    if command == "s":
        product=input("Enter a product name: ")
        #iterates through each product name in product dictionary
        for key in inventory.keys():
            #if product is found, information of product is printed
            if key == product:
                print('We sell "',product,'" at ', inventory[key][0],' per unit', sep ='')
                print("We currently have", inventory[key][1], "in stock")
                print()
                found += 1
        #runs if product is not found
        if found == 0:
            print("Sorry, we don't sell ",'"',product, '"', sep = '')
            print()
        
    #lists product information   
    if command == "l":
        

        #iterates through each item in product list and checks which product name's length is the longest
        for key in inventory.keys():
            length = len(key)
            if length > longestItem:
                         longestItem = length+3 #+3 for extra spacing

                         
        #length of longest item is used to format table of products, prices and quantity
        #prints titles of table
        print((format("Product","<" + str(longestItem)+"s")), (format("Price","<" + str(longestItem)+"s")),"Quantity")

        #prints each item in every list, formatted
        for key in inventory.keys():
            
            product = key
            price = format(float(inventory[key][0]),'.2f')
            
            quantity = inventory[key][1]
            print(format(product,"<" + str(longestItem)+"s"),format(price,"<" + str(longestItem)+"s"),quantity)
        print()
    #adds a new product to list
    if command == "a":
        while True:
            newProduct = input("Enter a new product name:")
            #iterates through product list and checks if product exists
            for key in inventory.keys():
                if key == newProduct:
                    print("Sorry, we already sell that product. Try again.")
                    print()
                else:
                    found += 1 #reusing counter to break out of while loop
                    break #breaks out of for loop
            if found > 0:
                break #breaks out of while loop if input is valid
            
        #makes sure product cost isn't less then or equal to 0       
        newCost = validate("Enter a product cost:","float",0)
        
        #makes sure input isn't negative or above 100
        newQuantity =validate("How many of these products do we have?: ","integer",0,100)

        #turns values into a list 
        stringValues = str(newCost) + ',' + str(newQuantity)
        listValues = stringValues.split(',')

        #turns values into a float and int so we can do calculations with it for the report
        listValues[0] = float(listValues[0])
        listValues[1] = int(listValues[1])
            
        #adds new product, its cost and quantity to dictionary
        inventory[newProduct] = listValues

        print("Product added!")
        print()

    if command == "r":
        productDel = input("Enter a product name to remove:")

        #removes item in dictionary if inputted product name exists in dictionary
        for key in inventory.keys():
            if key == productDel:
                del inventory[key]
                print("Product removed!")
                print()
                found+= 1
                break     
            else:
                found = 0
        if found == 0:
            print("Product does not exist.")
            print()

    if command == "u":
        productMod = input("Enter a product name to modify:")

        #checks if product inputted is in product list
        if productMod in inventory:
            print("What would you like to update?")
            mod = input("(n)ame, (c)ost or (q)uantity: ")
            mod = mod.lower()
            if mod == "n":
                while True:
                    newName = input("Enter a new name: ")
                    #checks if name already exists
                    if newName in inventory:
                        print("Duplicate name!")
                    else:
                        #stores existing values of product to be replaced
                        values = inventory[productMod]
                        

                        #deletes product and creates new key with the same values
                        del inventory[productMod]
                        inventory[newName]= values
                                        
                        break #breaks out of while loop
                    
                print("Product name has been updated")
                print()
                

            if mod == "c":
                        
                #makes sure new cost is valid             
                newCost = validate("Enter a product cost:","float",0)
                
                #replaces old cost with new cost at specified location in list
                cost = inventory[productMod]
                
                cost[0] = newCost
                
                

                inventory[productMod] = cost
                
                        
                print("Product cost has been updated")
                print()
                        
                    
            if mod == "q":
                
                #makes sure input isn't negative or above 100
                newQuantity =validate("How many of these products do we have?: ","integer",0,100)

        
                #replaces old quantity with new quantity at specific index in list
                quantity = inventory[productMod]
                quantity[1] = newQuantity
                
                inventory[productMod]= quantity
                
                print("Product quantity has been updated")
                print()
                
                
            #if input is invalid, error message is printed   
            if mod != "n" and mod != "c" and mod != "q":
                print("Invalid option")
                print()

                    
        #error message prints if user enters non-existent product   
        else:
            print("Product doesn't exist. Can't update")
            print()

    if command == "e":
       
        #creates list of all dictionary values
        biglist = []
        for value in inventory.values():
            biglist += value
        

        #creates only a list of prices
        prices = biglist[::2]
        #creates a list of only quantities
        quantities = biglist[1::2]

        #keeps track of total price
        total = 0
    
        #iterates for the amount of items in dictionary
        for i in range(len(prices)):
            total += prices[i] * quantities[i]  #multiplies price of each item by its quantity
        
        print("Total cost of all items in inventory: ", format(total,'.2f'))
        


        #finding lowest and highest values:
        #sorts prices from greatest to smallest
        prices.sort()

        #finds lowest and highest prices
        lowestPrice = prices[0]
        highPrice = prices[-1]

        #checks each key
        for key in inventory.keys():

            #checks if lowest price is in any of the keys' values
            if lowestPrice in inventory[key]:
                item = key
                break
        #formats price to two decimal places
        lowestPrice = format(lowestPrice,'.2f')
        #prints lowest priced item
        print("Lowest priced item: ",lowestPrice, "is ", item)
        

        #finds key with the highest price in its value
        for key in inventory.keys():
            if highPrice in inventory[key]:
                item = key
                break

        #formats price to two decimal places
        highPrice = format(highPrice, '.2f')
        #prints highest priced item
        print("Highest priced item: ", highPrice , "is", item)
        print()
        
