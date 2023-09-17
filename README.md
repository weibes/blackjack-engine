# Number Crunching Black Jack - Free Bet version

This is just a quick monte carlo/data crunching experiment to see what the house edge is on the free bet version of blackjack. Its mainly going to consist of a few tests:

1. Generating a basic strategy, and seeing what the house edge is on this strategy
2. Potentially generating some sort of "card counting" strategy for free bet, and seeing how much it can reduce house edge
3. Adding of configuration to allow for calculation of other variants (H/S17, surrender, side pot bets, etc.)


## Free Bet Rules
Free Bet is a variation of standard blackjack, with 2 major rule changes: 

1. Doubles on 9, 10, or 11 and any split (except 10s) are free
2. if the dealer gets 22, then everyone either loses or pushes (i.e., no win except for an initial blackjack)

## Assumed House Rules
H17, no surrender, can't redoubles A's, BJ pays 3:2 
### Side pots:

Pot of gold: This side bet just gives you a payout, depending on how many free bet coins you collect. So if you collect 1 coin, then you get a 1:1 payout.

| # of free bets  | Payout | 
|-----------------|--------|
| 1               | 1      | 
| 2               | 10     |
| 3               | 30     |
| 4               |  60    |
| 5               |  100   |
| 6               |  300   |
| 7               |  1000  |

Push 22: This side bet gives you a payout if the dealer gets 22.

| Dealer Hand  | Payout | 
|-----------------|--------|
| Bust not 22  | Lose    | 
| Other 22     | 8   |
| Same Color 22| 20     |
| Same Suit 22 | 50     |