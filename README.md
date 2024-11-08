# Trick-or-Treat-House-Wait-Times

## Members :

<li>Emmanuel Montoya</li>
<li>Rouni Assaf</li>

## Description :

As you go trick-or-treating on Halloween night, you visit a series of houses in a
neighborhood, each offering a different amount of candy. You have an array
houseCandies, where houseCandies[i] represents the amount of candy available at the
[i]th house you visit.

Your goal is to return an array waitHouses such that waitHouses[i] is the number of
houses you have to visit after the [i]th house to find one that offers more candy. If there is
no future house with more candy, set waitHouses[i] = 0.
Input: A positive integer array houseCandies where each element represents the candy
available at each house.
Output: A positive integer array waitHouses where each element represents the number
of houses to wait until encountering a house with more candy, or 0 if no such house
exists.

## Sample 1:
<p>Input: houseCandies = [3, 5, 8, 2, 1, 4, 10, 6]</p>
<p>Output: waitHouses = [1, 1, 4, 2, 1, 1, 0, 0]</p>

## Sample 2:
<p>Input: houseCandies = [2, 4, 6, 9]</p>
<p>Output: waitHouses = [1, 1, 1, 0]</p>

## Sample 3:
<p>Input: houseCandies = [7, 9, 8, 5, 11]</p>
<p>Output: waitHouses = [1, 3, 2, 1, 0]</p>


<b>**Optional Constraint :
Can you solve the problem in linear time complexity?</b>

