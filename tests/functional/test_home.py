import time

def test_index_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Verticle Tank Maintance" in res.data 
  


def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    print("-- /about GET test")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Verticle Tank Maintance" in res.data


def test_estimate_info_radius_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/estimate_info' route is requested (GET)
    THEN check that the user is redirected to the home page
    """
    print("-- /estimate_info GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate_info')
        assert res.status_code == 200
        assert b"Radius" in res.data

def test_estimate_info_height_route(app, client):
    print("-- /estimate_info GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate_info')
        assert res.status_code == 200
        assert b"Height" in res.data


def test_estimate_functionality(app, client):

    print("-- /estimate_info 'height' POST test")
    # Functional test - it puts POST data in the age route and looks for the correct value to be returned
    # individual functions to perform the calculations are tested in the Unit tests
    with app.test_client() as test_client:
        # pass in the data use Chrome Developer Tools -> Network -> Click on page -> Payload
        # passing future age value as 'x' because I look for the key(future_age), not the value in app.py if/then stmt
        data = {"height":"360", "radius":"180"} 
        res = test_client.post('/estimate_info', data=data)
        assert res.status_code == 200 
        assert b"$141300.0" in res.data 




