def date(day, month, year):
    try:
        if day <= 0 or month <= 0 or year <= 0:
            raise ValueError
        if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            raise ValueError
        elif month in [4, 6, 9, 11] and day > 30:
            raise ValueError
        elif month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if day > 29:
                    raise ValueError
            elif day > 28:
                raise ValueError
        elif type(date) != int or type(month) != int or type(year) != int:
            raise TypeError
    except ValueError:
        return print('False')
    except TypeError:
        return print('Wrong type of date')
    return print('True')


date(30, 2, 2000)  # вернет False, так как это високосный год
