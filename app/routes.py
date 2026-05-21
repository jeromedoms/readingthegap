from flask import Blueprint, render_template
from app.services import (
    get_overview_stats,
    get_non_readiness_chart,
    get_proficiency_chart,
    get_systemic_factors_chart,
    get_interventions_chart,
)

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template(
    "index.html",
    overview=get_overview_stats(),
    non_readiness=get_non_readiness_chart(),
    proficiency=get_proficiency_chart(),
    systemic_factors=get_systemic_factors_chart(),
    interventions=get_interventions_chart(),
)