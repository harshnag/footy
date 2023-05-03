import unittest

class SoccerGameTest(unittest.TestCase):

    def test_init(self):
        # Test that the game is initialized correctly
        game = SoccerGame()
        self.assertEqual(game.field, [[0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(game.home_team, ["home", "home", "home", "home", "home", "home"])
        self.assertEqual(game.away_team, ["away", "away", "away", "away", "away", "away"])
        self.assertEqual(game.time, 1)
        self.assertEqual(game.possession, 1)
        self.assertEqual(game.player, 1)
        self.assertEqual(game.direction, "up")
        self.assertEqual(game.home_score, 0)
        self.assertEqual(game.away_score, 0)

    def test_move_ball(self):
        # Test that the ball can be moved in all directions
        game = SoccerGame()
        game.move_ball("up")
        self.assertEqual(game.field[0][5], 0)
        self.assertEqual(game.field[5][5], 1)
        game.move_ball("down")
        self.assertEqual(game.field[5][5], 0)
        self.assertEqual(game.field[0][5], 1)
        game.move_ball("left")
        self.assertEqual(game.field[5][0], 0)
        self.assertEqual(game.field[5][5], 1)
        game.move_ball("right")
        self.assertEqual(game.field[5][5], 0)
        self.assertEqual(game.field[5][0], 1)
        game.move_ball("shoot")
        self.assertEqual(game.home_score, 1)
        self.assertEqual(game.away_score, 0)

    def test_check_goal(self):
        # Test that a goal is scored when the ball reaches the end of the field
        game = SoccerGame()
        game.field[0][5] = 1
        game.check_goal()
        self.assertEqual(game.home_score, 1)
        self.assertEqual(game.away_score, 0)
        game.field[5][0] = 2
        game.check_goal()
        self.assertEqual(game.home_score, 0)
        self.assertEqual(game.away_score, 1)

    def test_is_game_over(self):
        # Test that the game is over when the time limit is reached
        game = SoccerGame()
        game.time = 90
        self.assertTrue(game.is_game_over())

    def test_play_game(self):
        # Test that the game can be played from start to finish
        game = SoccerGame()
        game.play_game()
        self.assertEqual(game.home_score, 1)
        self.assertEqual(game.away_score, 1)

if __name__ == "__main__":
    unittest.main()
