// Define counter variable
var i = 0

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands
while (i < hands.length) {
    // Find and print number of points to bust
    println(pointsToBust(hands(i)))
    // Increment the counter variable
    i += 1
}