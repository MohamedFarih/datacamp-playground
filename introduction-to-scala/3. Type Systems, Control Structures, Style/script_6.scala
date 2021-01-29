def pointsToBust(hand: Int) = {
    // If the hand is a bust, 0 points remain
    if (bust(hand))
    println(0)
    // Otherwise, calculate the difference between 21 and the current hand
    else
    println(21 - hand)
}


// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands, finding each hand's number of points to bust
hands.foreach(pointsToBust)