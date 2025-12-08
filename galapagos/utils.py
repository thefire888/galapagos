import random


class Utils:
    def random_sex() -> str:
        return "M" if random.randint(0, 1) == 0 else "F"

    def get_total_cumulative_fit(available_individuals: list):
        cumulative_fit = 0
        for individual in available_individuals:
            cumulative_fit += individual[0].fitness * individual[1]
        return cumulative_fit

    def select_individual(available_individuals: list) -> 'Individual':
        # In probability theory, this is known
        # as sampling from a discrete distribution.
        cumulative_fit = 0
        total_cumulative_fit = (Utils.get_total_cumulative_fit(available_individuals))
        rand = random.uniform(0, total_cumulative_fit)
        for individual in available_individuals:
            cumulative_fit += individual[0].fitness * individual[1]
            if cumulative_fit > rand:
                return individual[0]

        if cumulative_fit <= rand:
            raise Exception("Valor aleatório não mapeia para "
                            "nenhum indivíduo")

    def get_max_sample(options_with_odds: list):
        max_sample = 0
        for option_with_odd in options_with_odds:
            odd = option_with_odd[1]
            max_sample += odd
        return max_sample

    def sample_from_distribution(options_with_odds: list):
        # In probability theory, this is known
        # as sampling from a discrete distribution.
        sample = 0
        max_sample = (Utils.get_max_sample(options_with_odds))
        rand = random.uniform(0, max_sample)
        for option_with_odd in options_with_odds:
            option = option_with_odd[0]
            odd = option_with_odd[1]
            sample += odd
            if sample > rand:
                return option

        if sample <= rand:
            raise Exception("Valor aleatório não mapeia para "
                            "nenhum indivíduo")
