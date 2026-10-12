import random

print("random function:", random.random())
print("random integer:",random.randint(1,50))
print("random float:",random.uniform(1,50))
print("random choice:",random.choice(("oppo","vivo","realme","oneplus","samsung","apple",
                                      "motorola","nokia", "lenovo","mi","iqoo","infinix",
                                      "lava","micromax","honor","poco","redmi","itel","gionee")))
print("choice repted:",random.choices(range(1,6),k=3))
print("random sample:",random.sample(range(1,100),5))
