from app.database.queries import (
    get_user_history,
    get_leaderboard
)


def get_user_analytics(username):

    return get_user_history(username)


def fetch_leaderboard():

    return get_leaderboard()