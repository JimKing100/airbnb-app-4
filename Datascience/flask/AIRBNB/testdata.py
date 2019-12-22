from AIRBNB.models import DB, listings


def add_test_data():
    DB.session.add(listings(id=1,
                            user_id=1,
                            property_type_id=2,
                            neighborhood_id=1,
                            room_types='Entire home/apt',
                            accommodates=4,
                            bedrooms=2,
                            bathrooms=2,
                            beds=2,
                            listing_url='http://test.com',
                            title='test title',
                            picture_url='http://test.com',
                            city='Austin',
                            state='TX',
                            zip=77777,
                            country='USA',
                            latitude=78,
                            longitude=80
                            ))
    DB.session.commit()
