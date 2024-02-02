from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .helpers import get_symbols, lookup, usd
from .forms import QuoteForm, BuySellForm
from .models import Portofolio, Contract
from decimal import Decimal

# Create your views here.


@login_required(login_url='/login')
def homepage(request):
    """Show portfolio of stocks"""

    # Keep track of total value for current portofolio
    total = Decimal(0)

    # Get user portofolio
    portofolio = request.user.portofolio.all()

    stocks = []
    if portofolio is not None:
        for p in portofolio:
            if p.shares > 0:
                quote = lookup(p.symbol)
                shares_price = Decimal(p.shares * quote.get('price'))
                total = total + shares_price

                item = {}
                item['symbol'] = p.symbol
                item['shares'] = p.shares
                item['name'] = quote.get('name')
                item['price'] = usd(quote.get('price'))
                item['total'] = usd(p.shares * quote.get('price'))
                stocks.append(item)
            else:
                continue

    total = total + request.user.cash
    return render(request=request, template_name='main/homepage.html', context={'cash': usd(request.user.cash), 'total': usd(total), 'stocks': stocks})


@login_required(login_url='/login')
def quote(request):
    """Get stock quote."""

    # User reached route via POST
    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            symbol = form.cleaned_data.get('symbol')
            quote = lookup(symbol)
            if quote is not None:
                # Redirect the user to quoted page
                return render(request=request, template_name="main/quoted.html", context={'quote': quote})
            else:
                messages.error(request, "Symbol not found!")
        else:
            messages.error(request, "Invalid form!")

    # User reached route via GET
    form = QuoteForm()
    return render(request=request, template_name='main/quote.html', context={'form': form})


@login_required
def buy(request):
    """Buy shares of stock"""

    # User reached route via POST
    if request.method == 'POST':
        form = BuySellForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data.get('symbol').upper()
            shares = form.cleaned_data.get('shares')

            quote = lookup(symbol)
            if quote is not None:
                shares_price = Decimal(shares * quote.get('price'))

                if request.user.cash.compare(shares_price) > 0:
                    try:
                        p = Portofolio.objects.get(user=request.user, symbol=symbol)
                    except:
                        p = Portofolio(symbol=symbol, shares=shares)
                        p.save()
                        request.user.portofolio.add(p)
                    else:
                        p.shares += shares
                        p.save()
                    finally:
                        c = Contract(symbol=symbol, shares=shares, price=quote.get('price'))
                        c.save()
                        request.user.contracts.add(c)

                        request.user.cash = request.user.cash - shares_price
                        request.user.save()

                        messages.info(request=request, message='Bought!')
                        return redirect('/')
                messages.error(request=request, message='Insufficient cash!')
            else:
                messages.error(request=request, message='Invalid symbol!')
        else:
            messages.error(request=request, message='Invalid form!')

    # User reached route via GET
    form = BuySellForm()
    return render(request=request, template_name='main/buy.html', context={'form': form})


@login_required
def sell(request):
    """Sell shares of stock"""

    # User reached route via POST
    if request.method == 'POST':
        form = BuySellForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data.get('symbol').upper()
            shares = form.cleaned_data.get('shares')

            quote = lookup(symbol)
            if quote is not None:
                try:
                    p = Portofolio.objects.get(user=request.user, symbol=symbol)
                except:
                    messages.error(request=request,
                                   message='You didn\'t own the given stock!')
                else:
                    if p.shares >= shares:
                        p.shares -= shares
                        p.save()

                        c = Contract(symbol=symbol, shares=shares, price=quote.get('price'), type='SELL')
                        c.save()
                        request.user.contracts.add(c)

                        shares_price = Decimal(shares * quote.get('price'))
                        request.user.cash = request.user.cash + shares_price
                        request.user.save()

                        messages.info(request=request, message='Sold!')
                        return redirect('/')
                    else:
                        messages.error(request=request, message='Too much shares!')
            else:
                messages.error(request=request, message='Invalid symbol!')
        else:
            messages.error(request=request, message='Invalid form!')

    # User reached route via GET
    form = BuySellForm()
    return render(request=request, template_name='main/sell.html', context={'form': form})


@login_required
def history(request):
    """Show history of transactions"""

    # Keep track of user's history
    history = list()

    # Get user's contracts
    contracts = request.user.contracts.all()

    # Create history's events
    for contract in contracts:
        if contract.type == 'SELL':
            contract.shares = -contract.shares
        
        contract.price = usd(contract.price)
        history.append(contract)

    # Render history page
    return render(request=request, template_name="main/history.html", context={'history': history})

