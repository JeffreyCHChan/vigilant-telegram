import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time

style.use("ggplot")

SIZE = 10
HM_EPISODES = 25000
MOVE_PENALTY = 2
FOOD_REWARD = 30
epsilon = .9 # can change this
EPS_DECAY = .9998
SHOW_EVERY = 2

start_q_table = "qtable - 1577313017.pickle" #Could pass a q-table we made already and seed at this point
#qtable - 1577309420.pickle
LEARNING_RATE = 0.1
DISCOUNT = 0.95

PLAYER_N = 1
FOOD_N =2

d = {1:(255,175,0), # blue is player
     2:(0,255,0)} #colour of dot

class Blob:
    def __init__(self):
        self.x = np.random.randint(0,SIZE)
        self.y = np.random.randint(0,SIZE) #location of starting y
    def __str__(self):
        return f"{self.x}, {self.y}"
    def __sub__(self, other):
        return(self.x - other.x, self.y - other.y)

    def action(self,choice):
        if choice == 0:
            self.move(x=1) #unidirectional movement
        elif choice == 1:
            self.move(x=-1)
        elif choice == 2:
            self.move(y=-1)
        elif choice ==3:
            self.move(y=1)
        pass
    def move(self,x=False,y=False):
        if not x:
            self.x += np.random.randint(-1,2)
        else:
            self.x += x
        if not y:
            self.y += np.random.randint(-1,2)
        else:
            self.y += y
        if self.x < 0: #boundary handling
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1

if start_q_table is None: #q-table craetion
    q_table = {}
    for x1 in range(-SIZE+1, SIZE):
        for y1 in range(-SIZE + 1, SIZE):
            q_table[(x1,y1)] = [np.random.uniform(-5,0) for i in range(4)]
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

episode_rewards = []
for episode in range(HM_EPISODES):
    player = Blob()
    food = Blob()

    if episode% SHOW_EVERY == 0:
        print(f" on #{episode}, epsilon: {epsilon}")
        print(f"{SHOW_EVERY} ep mean{np.mean(episode_rewards[-SHOW_EVERY:])}")
        show =True
    else:
        show = False

    episode_reward = 0
    for i in range(200): #num of steps we take, we could add as parameter later
        obs = (player - food)
        if np.random.random() > epsilon:
            action = np.argmax(q_table[obs])
        else:
            action = np.random.randint(0,4)
        player.action(action)

        #maybe letting food move
        #food.move()

        if player.x == food.x and player.y == food.y:
            reward = FOOD_REWARD
        else:
            reward = -MOVE_PENALTY # if player hasn't reached goal
        new_obs = (player-food)
        max_future_q = np.max(q_table[new_obs])
        current_q = q_table [obs][action]
        if reward == FOOD_REWARD:
            new_q = FOOD_REWARD
        else:
            new_q = (1-LEARNING_RATE) * current_q + LEARNING_RATE*(reward*DISCOUNT*max_future_q)
        q_table[obs][action] = new_q

        if show:
            env = np.zeros((SIZE,SIZE,3), dtype=np.uint8)
            env[food.x][food.y] = d[FOOD_N]
            env[player.x][player.y] = d[PLAYER_N]

            img = Image.fromarray(env,"RGB" )
            img = img.resize((300,300))
            cv2.imshow("", np.array(img))
            if reward ==  FOOD_REWARD:
                if cv2.waitKey(500) & 0xFF == ord("q"):
                    break
            else:
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        episode_reward += reward
        if reward == FOOD_REWARD:
            break
    episode_rewards.append(episode_reward)
    epsilon  *= EPS_DECAY
moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,)) / SHOW_EVERY, mode = "valid")

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()

with open(f"qtable - {int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)