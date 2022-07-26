def get_cleaned_data(raw_data):
    form = PromoCodeForm(raw_data)
    if form.is_valid():
        res = raw_data.cleaned_data
    else:
        res = {}
    return res
