# Sample Arrays
houseCandies1 = [3, 5, 8, 2, 1, 4, 10, 6]
houseCandies2 = [2, 4, 6, 9]
houseCandies3 =  [7, 9, 8, 5, 11]

# Array that will hold the values to be returned
waitHouses = []

# Initial For loop to check for first index item
for i in range(len(houseCandies1)):
    # Current value is bigger
    wait_time = 0

    # Second For loop to be comparing values with the current one
    for j in range(i + 1, len(houseCandies1)):
        # If the next value is bigger, substract the index value
            # difference to know how many indices farther away from
            # current is the next house with more candies, then break
        if houseCandies1[j] > houseCandies1[i]:
            wait_time = j - i
            break

    # Append the value in wait_time for the new array
    waitHouses.append(wait_time)

# Display waitHouses Array
print("waitHouses:", waitHouses)