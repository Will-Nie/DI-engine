from easydict import EasyDict

walker2d_sac_default_config = dict(
    exp_name = 'walker2d_trex_sac',
    env=dict(
        manager=dict(shared_memory=True, force_reproducibility=True),
        env_id='Walker2d-v3',
        norm_obs=dict(use_norm=False, ),
        norm_reward=dict(use_norm=False, ),
        collector_env_num=1,
        evaluator_env_num=8,
        use_act_scale=True,
        n_evaluator_episode=8,
        stop_value=6000,
    ),
    reward_model=dict(
        type='trex',
        algo_for_model='sac',
        env_id='Walker2d-v3',
        min_snippet_length=30,
        max_snippet_length=100,
        checkpoint_min=100,
        checkpoint_max=900,
        checkpoint_step=100,
        learning_rate=1e-5,
        update_per_collect=1,
        expert_model_path='/Users/nieyunpeng/Documents/open-sourced-algorithms/TREX/dizoo/mujoco/config/walker2d_sac',
        reward_model_path='./walker2d.params',
        continuous=True,
        offline_data_path='walker2d_trex_sac/suboptimal_data.pkl',
    ),
    policy=dict(
        cuda=True,
        random_collect_size=10000,
        model=dict(
            obs_shape=17,
            action_shape=6,
            twin_critic=True,
            actor_head_type='reparameterization',
            actor_head_hidden_size=256,
            critic_head_hidden_size=256,
        ),
        learn=dict(
            update_per_collect=1,
            batch_size=256,
            learning_rate_q=1e-3,
            learning_rate_policy=1e-3,
            learning_rate_alpha=3e-4,
            ignore_done=False,
            target_theta=0.005,
            discount_factor=0.99,
            alpha=0.2,
            reparameterization=True,
            auto_alpha=False,
        ),
        collect=dict(
            n_sample=1,
            unroll_len=1,
        ),
        command=dict(),
        eval=dict(),
        other=dict(replay_buffer=dict(replay_buffer_size=1000000, ), ),
    ),
)

walker2d_sac_default_config = EasyDict(walker2d_sac_default_config)
main_config = walker2d_sac_default_config

walker2d_sac_default_create_config = dict(
    env=dict(
        type='mujoco',
        import_names=['dizoo.mujoco.envs.mujoco_env'],
    ),
    env_manager=dict(type='subprocess'),
    policy=dict(
        type='sac',
        import_names=['ding.policy.sac'],
    ),
    replay_buffer=dict(type='naive', ),
)
walker2d_sac_default_create_config = EasyDict(walker2d_sac_default_create_config)
create_config = walker2d_sac_default_create_config
