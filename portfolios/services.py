from decimal import Decimal

from django.db.models import Sum, Q, F

from transactions.models import Transaction


def get_portfolio_summary(user):
    '''
    Returns consolidated portfolio data for the given user:
    - total_invested: sum of buys - sum of sells (value without fees)
    - positions: list of assets with positive balance, including
      quantity, average price and invested value per asset
    '''
    transactions = Transaction.objects.filter(user=user)

    if not transactions.exists():
        return {
            'total_invested': Decimal('0.00'),
            'positions': [],
            'num_assets': 0,
            'largest_position': None,
            'last_transaction': None,
        }

    asset_data = {}

    for txn in transactions.select_related('asset'):
        asset = txn.asset
        ticker = asset.ticker

        if ticker not in asset_data:
            asset_data[ticker] = {
                'asset': asset,
                'buy_quantity': Decimal('0'),
                'buy_total': Decimal('0'),
                'sell_quantity': Decimal('0'),
                'sell_total': Decimal('0'),
            }

        if txn.transaction_type == 'BUY':
            asset_data[ticker]['buy_quantity'] += txn.quantity
            asset_data[ticker]['buy_total'] += txn.quantity * txn.unit_price
        else:
            asset_data[ticker]['sell_quantity'] += txn.quantity
            asset_data[ticker]['sell_total'] += txn.quantity * txn.unit_price

    positions = []
    total_invested = Decimal('0.00')

    for ticker, data in asset_data.items():
        net_quantity = data['buy_quantity'] - data['sell_quantity']

        if net_quantity > 0:
            avg_price = data['buy_total'] / data['buy_quantity'] if data['buy_quantity'] > 0 else Decimal('0')
            invested_value = net_quantity * avg_price

            positions.append({
                'asset': data['asset'],
                'quantity': net_quantity,
                'avg_price': avg_price.quantize(Decimal('0.01')),
                'invested_value': invested_value.quantize(Decimal('0.01')),
            })

            total_invested += invested_value

    positions.sort(key=lambda p: p['invested_value'], reverse=True)

    largest_position = positions[0] if positions else None
    last_transaction = transactions.first()

    return {
        'total_invested': total_invested.quantize(Decimal('0.01')),
        'positions': positions,
        'num_assets': len(positions),
        'largest_position': largest_position,
        'last_transaction': last_transaction,
    }


def get_composition_by_type(user):
    '''
    Returns the percentage invested per asset type.
    Example: [{'type': 'Ação', 'type_code': 'STOCK', 'total': 5000, 'percentage': 50.0}, ...]
    '''
    summary = get_portfolio_summary(user)
    positions = summary['positions']
    total_invested = summary['total_invested']

    if not positions or total_invested == 0:
        return []

    type_totals = {}
    for pos in positions:
        asset_type = pos['asset'].asset_type
        type_display = pos['asset'].get_asset_type_display()

        if asset_type not in type_totals:
            type_totals[asset_type] = {
                'type': type_display,
                'type_code': asset_type,
                'total': Decimal('0'),
            }

        type_totals[asset_type]['total'] += pos['invested_value']

    composition = []
    for data in type_totals.values():
        percentage = (data['total'] / total_invested * 100).quantize(Decimal('0.01'))
        composition.append({
            'type': data['type'],
            'type_code': data['type_code'],
            'total': data['total'].quantize(Decimal('0.01')),
            'percentage': float(percentage),
        })

    composition.sort(key=lambda c: c['percentage'], reverse=True)

    return composition
