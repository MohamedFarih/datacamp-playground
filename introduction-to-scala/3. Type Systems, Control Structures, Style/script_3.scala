def pointsToBust(hand: Int): Int = {
    // If the hand is a bust, 0 points remain
    if (bust(hand))
    0
    // Otherwise, calculate the difference between 21 and the current hand
    else
    21 - hand
}


// Test pointsToBust with 10♠ and 5♣
val myHandPointsToBust = pointsToBust(tenSpades + fiveClubs)
println(myHandPointsToBust)