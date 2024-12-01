import os
import time
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


ENCODED_AES_KEY = base64.b64encode(b"43616e5f646563727970745f6d655f21").decode()  
ENCODED_AES_IV = base64.b64encode(b"31743366357337653974313131323133").decode()  

class PongAnimation:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.ball = [self.width // 2, self.height // 2]
        self.ball_velocity = [random.choice([1, -1]), random.choice([1, -1])]
        self.paddle1 = [self.height // 2 - 3, self.height // 2 + 3]
        self.paddle2 = [self.height // 2 - 3, self.height // 2 + 3]
        self.start_time = time.time()
        self.game_duration = 10  

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("+" + "-" * (self.width - 2) + "+")
            else:
                row = "|"
                for j in range(self.width - 2):
                    if j == self.ball[0] and i == self.ball[1]:
                        row += "O"
                    elif j == 1 and i >= self.paddle1[0] and i <= self.paddle1[1]:
                        row += "|"
                    elif j == self.width - 3 and i >= self.paddle2[0] and i <= self.paddle2[1]:
                        row += "|"
                    else:
                        row += " "
                row += "|"
                print(row)
        print("+" + "-" * (self.width - 2) + "+")
        print(f"Time Left: {max(0, self.game_duration - (time.time() - self.start_time)):.1f}s")
    
    def move_ball(self):
        if self.ball[1] <= 0 or self.ball[1] >= self.height - 1:
            self.ball_velocity[1] *= -1
        if self.ball[0] <= 1 and self.paddle1[0] <= self.ball[1] <= self.paddle1[1]:
            self.ball_velocity[0] *= -1
        elif self.ball[0] >= self.width - 3 and self.paddle2[0] <= self.ball[1] <= self.paddle2[1]:
            self.ball_velocity[0] *= -1

        self.ball[0] += self.ball_velocity[0]
        self.ball[1] += self.ball_velocity[1]
    
    def play(self):
        while time.time() - self.start_time < self.game_duration:
            self.draw()
            self.move_ball()
            time.sleep(0.05)  

AES_KEY = bytes.fromhex(base64.b64decode(ENCODED_AES_KEY).decode())
AES_IV = bytes.fromhex(base64.b64decode(ENCODED_AES_IV).decode())
def encrypt_input(input_str, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(input_str.encode(), AES.block_size)  
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted).decode()  

def main():
    pong = PongAnimation()
    pong.play()

    print("\nGame Over! \nYour subscription has ended. Please enter the key to continue playing the game:")
    user_input = input("Enter: ")

    encrypted_input = encrypt_input(user_input, AES_KEY, AES_IV)

    flag = "xU5cNXeXeIL0aCBw0stJ5Q=="  
    if encrypted_input == flag:
        print(f"Flag is Cyberbenders{{{user_input}}}")
    else:
        print("Incorrect Key. Try again.")

if __name__ == "__main__":
    main()
