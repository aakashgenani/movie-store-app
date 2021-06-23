from tables.models import UserPurchase


def get_purchases_by_user_id(user_id):
    purchases = UserPurchase.query.filter_by(user_id=user_id).all()
    return purchases
