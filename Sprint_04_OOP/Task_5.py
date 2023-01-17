class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.game_over:
            self.words = [word]
            self.game_over = False
            return self.words, self.game_over
        elif not self.game_over:
            if len(self.words) != 0:
                if word not in self.words and self.words[-1][-1] == word[0]:
                    self.words.append(word)
                    return self.words
                else:
                    self.game_over = True
                    return "game over"

            else:
                self.words.append(word)
                return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.game_over)
print(my_gallows.play('apple'))
print(my_gallows.words)
print(my_gallows.play('ear'))
print(my_gallows.play('rhino'))
print(my_gallows.play('ocelot'))
print(my_gallows.game_over)
print("=" * 50)
print(my_gallows.play('oops'))
print("=" * 50)
print(my_gallows.game_over)
print("=" * 50)
print(my_gallows.words)


my_gallows = Gallows()
print(my_gallows.restart())
print("=" * 50)
print(my_gallows.words)
print("=" * 50)
print(my_gallows.game_over)
print("=" * 50)
print(my_gallows.play('hostess'))
print(my_gallows.game_over, False)
print(my_gallows.play('stash'))
print(my_gallows.play('hostess'))
print(my_gallows.words)



