# Texas Hold'em Poker Hands Kata - Starter

This is a starter repository for the Poker Hands coding kata. The goal is to implement a Texas Hold'em poker hand evaluator.

## Getting Started

This project uses Gradle for build and dependency management. You don't need to install Gradle - use the included wrapper.

### Build the project
```bash
./gradlew build
```

### Run tests
```bash
./gradlew test
```

### Project Structure

```
src/
├── main/java/com/kata/poker/    # Your production code goes here
└── test/java/com/kata/poker/    # Your test code goes here
```

## The Challenge

Implement a poker hand evaluator that can compare two 4-card poker hands and determine the winner.

### Poker Hand Rankings (from highest to lowest)

1. **Straight Flush**: Four cards in sequence, all of the same suit
2. **Four of a Kind**: Four cards of the same value
3. **Flush**: Four cards of the same suit
4. **Straight**: Four cards in sequence
5. **Three of a Kind**: Three cards of the same value
6. **Two Pair**: Two different pairs
7. **Pair**: Two cards of the same value
8. **High Card**: When no other hand applies, the highest card wins

### Card Representation

Each card has:
- **Suit**: Hearts (H), Spades (S), Clubs (C), Diamonds (D)
- **Value**: 2-10, Jack (J), Queen (Q), King (K), Ace (A)

Example cards: `2H` (Two of Hearts), `AS` (Ace of Spades), `KC` (King of Clubs)

### Example Input/Output

```
Input: "Black: 2H 3D 5S 9C  White: 2C 3H 4S 8C"
Output: "Black wins. - with high card: 9"

Input: "Black: 2H 4S 4C 2D  White: 2S 8S AS QS"
Output: "Black wins. - with two pair: 4 and 2"

Input: "Black: 2H 3D 5S 9C  White: 2C 3H 5C 9S"
Output: "Tie."
```

## Tips for the Kata

- Start with simple cases (high card comparison)
- Build incrementally, adding one hand type at a time
- Use Test-Driven Development (TDD)
- Consider using design patterns (Strategy, Factory, Visitor, etc.)
- Think about how to make your code extensible for new hand types

## Resources

- [PokerHands Kata on Coding Dojo](http://codingdojo.org/kata/PokerHands/)
- [List of Poker Hands on Wikipedia](https://en.wikipedia.org/wiki/List_of_poker_hands)

Good luck and have fun!
