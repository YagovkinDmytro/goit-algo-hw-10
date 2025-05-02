import pulp

# Initialize the model
model = pulp.LpProblem("Production optimization", pulp.LpMaximize)

# Define variables
Lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Quantity of product
Fruit_juice = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Integer')  # Quantity of product

# Objective function
model += Lemonade + Fruit_juice, "Total production"

# Add constraints
model += 2 * Lemonade + 1 * Fruit_juice <= 100 # Constraint for water
model += 1 * Lemonade <= 50  # Constraint for sugar
model += 1 * Lemonade <= 30  # Constraint for lemon juice
model += 2 * Fruit_juice <= 40  # Constraint for fruit puree

# Solution model
model.solve()

# Output results
print("Solution status:", pulp.LpStatus[model.status])
print("Produce products Lemonade:", Lemonade.varValue)
print("Produce products Fruit juice:", Fruit_juice.varValue)