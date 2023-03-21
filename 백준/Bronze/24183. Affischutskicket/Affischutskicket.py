env, pos, info = map(int, input().split())
env_w = 229 * 324 * env * 2
pos_w = 297 * 420 * pos * 2
info_w = 210 * 297 * info
total = (env_w + pos_w + info_w) * 0.000001
print(total)
