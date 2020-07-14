from gym.envs.registration import register

register(
    id='crawler-v0',
    entry_point='gym_crawler.envs:CrawlerEnv',
)