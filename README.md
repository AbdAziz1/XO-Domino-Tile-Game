# XO-Domino-Tile-Game

### The XO domino-tile game is played by 2 players using a square board. Players take turns to
enter the coordinates of 2 EMTPY squares (row-col, row-col) to place their domino-tiles, until
there is no possible move. We will illustrate the game using a 5x5 square board.

### Employ structured programming to develop this game with the following playing rules:
 At start of the game, prompt for the following:
 o Two unique names representing the of 2 players.
 o Size of the game board, that must be odd number and at least 3.
 The computer randomly decides which player to start and will take the symbol X.
The other player will take the symbol O.
 Each player in turn will place a domino-style tile that occupy 2 EMTPY squares.
 o Your program must validate the 2 squares that the player wanted to place
   the next tile.
 o In the above board, if a player enters 00 10 for his next tile, it is invalid as
   00 is already occupied.
o In the above board, if a player enters 11 12 for his next tile, it is invalid as
  12 is already occupied.
o If player enters 21 32 for his next tile, it is invalid as the 2 squares are not
  connected vertically or horizontally.
 Game ends when no player can place any more tile.
 Player with the most tiles on the board wins.
 If the result is a tie, repeat the game until a winner can be determined.
