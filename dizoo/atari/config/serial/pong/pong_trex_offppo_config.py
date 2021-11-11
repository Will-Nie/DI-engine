from copy import deepcopy
from ding.entry import serial_pipeline
from easydict import EasyDict

pong_ppo_config = dict(
    exp_name='pong_trex_offppo',
    env=dict(
        collector_env_num=16,
        evaluator_env_num=8,
        n_evaluator_episode=8,
        stop_value=20,
        env_id='PongNoFrameskip-v4',
        frame_stack=4,
        manager=dict(shared_memory=False, )
    ),
    reward_model=dict(
    type='trex',
    algo_for_model = 'ppo',
    env_id='PongNoFrameskip-v4',
    input_size=5,
    hidden_size=64,
    batch_size=64,
    learning_rate=1e-5,
    update_per_collect=1,
    expert_model_path='/Users/nieyunpeng/Documents/open-sourced-algorithms/TREX/dizoo/atari/config/serial/pong/ppo_offpolicy_pong',
    reward_model_path='./pong.params',
    load_path='',
    ),
    policy=dict(
        cuda=True,
        random_collect_size=2048,
        model=dict(
            obs_shape=[4, 84, 84],
            action_shape=6,
            encoder_hidden_size_list=[64, 64, 128],
            actor_head_hidden_size=128,
            critic_head_hidden_size=128,
            critic_head_layer_num=1,  # Todo, to solve generality problem
        ),
        learn=dict(
            update_per_collect=24,
            batch_size=128,
            # (bool) Whether to normalize advantage. Default to False.
            adv_norm=False,
            learning_rate=0.0002,
            # (float) loss weight of the value network, the weight of policy network is set to 1
            value_weight=0.5,
            # (float) loss weight of the entropy regularization, the weight of policy network is set to 1
            entropy_weight=0.01,
            clip_ratio=0.1,
        ),
        collect=dict(
            # (int) collect n_sample data, train model n_iteration times
            n_sample=1024,
            # (float) the trade-off factor lambda to balance 1step td and mc
            gae_lambda=0.95,
            discount_factor=0.99,
        ),
        eval=dict(evaluator=dict(eval_freq=1000, )),
        other=dict(replay_buffer=dict(
            replay_buffer_size=100000,
            max_use=5,
        ), ),
    ),
)
main_config = EasyDict(pong_ppo_config)

pong_ppo_create_config = dict(
    env=dict(
        type='atari',
        import_names=['dizoo.atari.envs.atari_env'],
    ),
    # env_manager=dict(type='subprocess'),
    env_manager=dict(type='base'),
    policy=dict(type='ppo_offpolicy'),
)
create_config = EasyDict(pong_ppo_create_config)

if __name__ == '__main__':
    serial_pipeline((main_config, create_config), seed=0)