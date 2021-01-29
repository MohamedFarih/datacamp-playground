// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Inform a player where their current hand stands
val informPlayer: String = {
    if (hand > 21)
    "Bust! :("
    else if (hand == 21)
    "Twenty-One! :)"
    else
    "Hit or stay?"
}

// Print the message
print(informPlayer)