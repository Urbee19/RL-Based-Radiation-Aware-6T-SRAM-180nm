def calculate_reward(state):
    Qcrit, SNM, Delay, Power, _, _ = state

    # Normalization (approx realistic scaling)
    Qnorm = Qcrit / 50
    SNMnorm = SNM / 300
    DelayNorm = Delay / 600
    PowerNorm = Power / 5

    reward = (0.5 * Qnorm +
              0.3 * SNMnorm -
              0.1 * DelayNorm -
              0.1 * PowerNorm)

    return reward
