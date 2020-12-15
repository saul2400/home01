# Prices:
price_pizza = 70.5
price_salade = 20
price_soup = 30

# Nr: 
nr_pizza = int( input("Nr of pizza:") )
nr_salade = int( input("Nr of salade:") )
nr_soup = int( input("Nr of soup:") )

# calcul:
total_pizza = price_pizza * nr_pizza
total_salade = price_salade * nr_salade
total_soup = price_soup * nr_soup

total = total_pizza + total_salade + total_soup

# Output:

print("##### Restaurant Menu #####")
print("#1. Pizza price:", price_pizza)
print("#2. Salade price:", price_salade)
print("#3. Soup price:", price_soup)
print("###########################")
print("# How many pizza/e do you want:", nr_pizza )
print("# How many salade/s do you want:", nr_salade )
print("# How many soup/s do you want:", nr_soup )
print("###########################")
print("# Pizza x", nr_pizza , "=", total_pizza)
print("# Salade x", nr_salade , "=", total_salade)
print("# Soup x", nr_soup , "=", total_soup)
print("###########################")
print("# Total cost:", total)
print("###########################")
