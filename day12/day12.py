# Day 12 - Namespaces: Local vs Global Scope

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# When you create a variable inside a function, it can only be 
# used inside the function, because it has local scope.
# If a variable is created outside functions, it has global scope.

## There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0] # Variable created inside block (if statement)

print(new_enemy) # It will be perfectly printed


## Modifying Global Scope

# Example 1: not recommended
enemies = 1

def increase_enemies():
    global enemies # Takes the global variable enemies inside the function
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Example 2: recommended (using return to modify a global variable)

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants. Put them in upper case so you remember that this
# is variable that should not be modified.

PI = 3.14159
URL = "https://www.google.com"