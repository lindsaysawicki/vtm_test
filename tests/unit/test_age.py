import app

def test_calculate_cost():

    print("\r")
    print(" -- calculate_total_cost unit test")
    assert app.calculate_total_area(3235.5) == 1.7444444444444445   #will change as the years progress


"""def test_calculate_future_age():
    
    GIVEN a user age
    WHEN that age is passed to this function
    THEN 10 years are added to the user's age
    
    print("-- calculate_future_age unit test")
    assert app.calculate_future_age(20) == 30  


def test_calculate_past_age():
     
    GIVEN a user age
    WHEN that age is passed to this function
    THEN 10 years are subtracted from the user's agee
    
    print("-- calculate_past_age unit test")
    assert app.calculate_past_age(20) == 10  """