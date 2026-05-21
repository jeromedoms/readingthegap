from app.data import (
    OVERVIEW_STATS,
    NON_READINESS,
    SCHOOL_PROFICIENCY,
    SYSTEMIC_FACTORS,
    INTERVENTIONS,
)


def get_overview_stats():
    return OVERVIEW_STATS


def get_non_readiness_chart():
    return [
        {
            "label": item["grade"],
            "value": item["value"],
        }
        for item in NON_READINESS
    ]


def get_proficiency_chart():
    return [
        {
            "label": item["school_classification"].replace(" School", ""),
            "value": item["value"],  # already in percent, no need to multiply
        }
        for item in SCHOOL_PROFICIENCY
    ]


def get_systemic_factors_chart():
    return [
        {
            "label": item["factor"],
            "value": item["value"],
            "description": item.get("description", ""),
        }
        for item in SYSTEMIC_FACTORS
    ]


def get_interventions_chart():
    return [
        {
            "label": item["strategy"],
            "pretest": item["pretest_mean"],
            "posttest": item["posttest_mean"],
            "gain": item["mean_gain"],
        }
        for item in INTERVENTIONS
    ]