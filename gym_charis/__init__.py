from gym.envs.registration import register

register(
    id='charis-v0',
    entry_point='gym_charis.envs:CharisEnv',
)
