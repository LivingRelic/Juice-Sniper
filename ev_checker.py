from prop_scraper import get_mock_odds

def check_for_ev_plays():
    projections = {
        "Jayson Tatum Points": 27.0,
        "Anthony Edwards PRA": 37.5
    }

    odds_data = get_mock_odds()
    alerts = []

    for player, books in odds_data.items():
        if player not in projections:
            continue
        projected = projections[player]
        for book, line in books.items():
            edge = projected - line
            if edge >= 2.0:
                alerts.append(
                    f"🟢 **{player}**: {line} on {book}, projected {projected} → **+{round(edge,1)}pt edge**"
                )
    return alerts