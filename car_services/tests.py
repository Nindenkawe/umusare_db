import unittest

from django.test import TestCase

from .models import User, Subscriber, Provider, Transaction, Car, Proposed_insucovers, Chauffeur_profile, Mechanic_profile, Book_Driver, Parkingfacility_profile, RoadAssistance, Ownership_Transfer, Vehicle_deregistration

from .serializers import UserSerializer, SubscriberSerializer, ProviderSerializer, TransactionSerializer, CarSerializer, Proposed_insucoversSerializer, Chauffeur_profileSerializer, Mechanic_profileSerializer, Book_DriverSerializer, Parkingfacility_profileSerializer, RoadAssistanceSerializer, Ownership_TransferSerializer, Vehicle_deregistrationSerializer

from .views import LoadUserAPIView, SubscriberAPIView, ProviderAPIView, TransactionAPIView, CarAPIView, Proposed_insucoversAPIView, Chauffeur_profileAPIView, Mechanic_profileAPIView, Book_DriverAPIView, Parkingfacility_profileAPIView, RoadAssistanceAPIView, Ownership_TransferAPIView, Vehicle_deregistrationAPIView


class UserTestCase(TestCase):

    def test_user_model(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword'))


class SubscriberTestCase(TestCase):

    def test_subscriber_model(self):
        subscriber = Subscriber.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Subscriber', email='testsubscriber@example.com', phone_number='1-800-555-1212')
        self.assertEqual(subscriber.user.username, 'testuser')
        self.assertEqual(subscriber.user.email, 'testuser@example.com')
        self.assertEqual(subscriber.name, 'Test Subscriber')
        self.assertEqual(subscriber.email, 'testsubscriber@example.com')
        self.assertEqual(subscriber.phone_number, '1-800-555-1212')


class ProviderTestCase(TestCase):

    def test_provider_model(self):
        provider = Provider.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Provider', email='testprovider@example.com', phone_number='1-800-555-1212', address='123 Main Street, Anytown, CA 12345')
        self.assertEqual(provider.user.username, 'testuser')
        self.assertEqual(provider.user.email, 'testuser@example.com')
        self.assertEqual(provider.name, 'Test Provider')
        self.assertEqual(provider.email, 'testprovider@example.com')
        self.assertEqual(provider.phone_number, '1-800-555-1212')
        self.assertEqual(provider.address, '123 Main Street, Anytown, CA 12345')


class TransactionTestCase(TestCase):

    def test_transaction_model(self):
        transaction = Transaction.objects.create(subscriber=Subscriber.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Subscriber', email='testsubscriber@example.com', phone_number='1-800-555-1212'), provider=Provider.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Provider', email='testprovider@example.com', phone_number='1-800-555-1212', address='123 Main Street, Anytown, CA 12345'), amount=100.00, description='Test transaction')
        self.assertEqual(transaction.subscriber.user.username, 'testuser')
        self.assertEqual(transaction.subscriber.user.email, 'testuser@example.com')
        self.assertEqual(transaction.subscriber.name, 'Test Subscriber')
        self.assertEqual(transaction.subscriber.email, 'testsubscriber@example.com')
        self.assertEqual(transaction.subscriber.phone_number, '1-800-555-1212')
        self.assertEqual(transaction.provider.user.username, 'testuser')
        self.assertEqual(transaction.provider.user.email, 'testuser@example.com')
        self.assertEqual(transaction.provider.name, 'Test Provider')
        self.assertEqual(transaction.provider.email, 'testprovider@example.com')
        self.assertEqual(transaction.provider.phone_number, '1-800-555-1212')
        self.assertEqual(transaction.provider.address, '123 Main Street, Anytown, CA 12345')
        self.assertEqual(transaction.amount, 100.00)
        self.assertEqual(transaction.description, 'Test transaction')


class CarTestCase(TestCase):

    def test_car_model(self):
        car = Car.objects.create(vin='1234567890', make='Toyota', model='Camry', year=2020, color='Blue', license_plate='ABC123')
        self.assertEqual(car.vin, '1234567890')
        self.assertEqual(car.make, 'Toyota')
        self.assertEqual(car.model, 'Camry')
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.color, 'Blue')
        self.assertEqual(car.license_plate, 'ABC123')


class Proposed_insucoversTestCase(TestCase):

    def test_proposed_insucovers_model(self):
        proposed_insucovers = Proposed_insucovers.objects.create(subscriber=Subscriber.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Subscriber', email='testsubscriber@example.com', phone_number='1-800-555-1212'), provider=Provider.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Provider', email='testprovider@example.com', phone_number='1-800-555-1212', address='123 Main Street, Anytown, CA 12345'), insurance_company='Test Insurance Company', policy_number='1234567890', coverage_amount=100000.00, start_date='2020-01-01', end_date='2020-12-31')
        self.assertEqual(proposed_insucovers.subscriber.user.username, 'testuser')
        self.assertEqual(proposed_insucovers.subscriber.user.email, 'testuser@example.com')
        self.assertEqual(proposed_insucovers.subscriber.name, 'Test Subscriber')
        self.assertEqual(proposed_insucovers.subscriber.email, 'testsubscriber@example.com')
        self.assertEqual(proposed_insucovers.subscriber.phone_number, '1-800-555-1212')
        self.assertEqual(proposed_insucovers.provider.user.username, 'testuser')
        self.assertEqual(proposed_insucovers.provider.user.email, 'testuser@example.com')
        self.assertEqual(proposed_insucovers.provider.name, 'Test Provider')
        self.assertEqual(proposed_insucovers.provider.email, 'testprovider@example.com')
        self.assertEqual(proposed_insucovers.provider.phone_number, '1-800-555-1212')
        self.assertEqual(proposed_insucovers.provider.address, '123 Main Street, Anytown, CA 12345')
        self.assertEqual(proposed_insucovers.insurance_company, 'Test Insurance Company')
        self.assertEqual(proposed_insucovers.policy_number, '1234567890')
        self.assertEqual(proposed_insucovers.coverage_amount, 100000.00)
        self.assertEqual(proposed_insucovers.start_date, '2020-01-01')
        self.assertEqual(proposed_insucovers.end_date, '2020-12-31')


class Chauffeur_profileTestCase(TestCase):

    def test_chauffeur_profile_model(self):
        chauffeur_profile = Chauffeur_profile.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Chauffeur', email='testchauffeur@example.com', phone_number='1-800-555-1212', license_number='1234567890', rating=5.0)
        self.assertEqual(chauffeur_profile.user.username, 'testuser')
        self.assertEqual(chauffeur_profile.user.email, 'testuser@example.com')
        self.assertEqual(chauffeur_profile.name, 'Test Chauffeur')
        self.assertEqual(chauffeur_profile.email, 'testchauffeur@example.com')
        self.assertEqual(chauffeur_profile.phone_number, '1-800-555-1212')
        self.assertEqual(chauffeur_profile.license_number, '1234567890')
        self.assertEqual(chauffeur_profile.rating, 5.0)


class Mechanic_profileTestCase(TestCase):

    def test_mechanic_profile_model(self):
        mechanic_profile = Mechanic_profile.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Mechanic', email='testmechanic@example.com', phone_number='1-800-555-1212', license_number='1234567890', rating=5.0)
        self.assertEqual(mechanic_profile.user.username, 'testuser')
        self.assertEqual(mechanic_profile.user.email, 'testuser@example.com')
        self.assertEqual(mechanic_profile.name, 'Test Mechanic')
        self.assertEqual(mechanic_profile.email, 'testmechanic@example.com')
        self.assertEqual(mechanic_profile.phone_number, '1-800-555-1212')
        self.assertEqual(mechanic_profile.license_number, '1234567890')
        self.assertEqual(mechanic_profile.rating, 5.0)


class Book_DriverTestCase(TestCase):

    def test_book_driver_model(self):
        book_driver = Book_Driver.objects.create(subscriber=Subscriber.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Subscriber', email='testsubscriber@example.com', phone_number='1-800-555-1212'), driver=Chauffeur_profile.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Driver', email='testdriver@example.com', phone_number='1-800-555-1212', license_number='1234567890', rating=5.0), pickup_location='123 Main Street, Anytown, CA 12345', dropoff_location='456 Elm Street, Anytown, CA 12345', pickup_date='2020-01-01', pickup_time='10:00 AM', dropoff_date='2020-01-02', dropoff_time='11:00 AM', status='pending')
        self.assertEqual(book_driver.subscriber.user.username, 'testuser')
        self.assertEqual(book_driver.subscriber.user.email, 'testuser@example.com')
        self.assertEqual(book_driver.subscriber.name, 'Test Subscriber')
        self.assertEqual(book_driver.subscriber.email, 'testsubscriber@example.com')
        self.assertEqual(book_driver.subscriber.phone_number, '1-800-555-1212')
        self.assertEqual(book_driver.driver.user.username, 'testuser')
        self.assertEqual(book_driver.driver.user.email, 'testuser@example.com')
        self.assertEqual(book_driver.driver.name, 'Test Driver')
        self.assertEqual(book_driver.driver.email, 'testdriver@example.com')
        self.assertEqual(book_driver.driver.phone_number, '1-800-555-1212')
        self.assertEqual(book_driver.driver.license_number, '1234567890')
        self.assertEqual(book_driver.driver.rating, 5.0)
        self.assertEqual(book_driver.pickup_location, '123 Main Street, Anytown, CA 12345')
        self.assertEqual(book_driver.dropoff_location, '456 Elm Street, Anytown, CA 12345')
        self.assertEqual(book_driver.pickup_date, '2020-01-01')
        self.assertEqual(book_driver.pickup_time, '10:00 AM')
        self.assertEqual(book_driver.dropoff_date, '2020-01-02')
        self.assertEqual(book_driver.dropoff_time, '11:00 AM')
        self.assertEqual(book_driver.status, 'pending')


class Parkingfacility_profileTestCase(TestCase):

    def test_parkingfacility_profile_model(self):
        parkingfacility_profile = Parkingfacility_profile.objects.create(name='Test Parking Facility', address='123 Main Street, Anytown, CA 12345', phone_number='1-800-555-1212', website='http://www.testparkingfacility.com/', rating=5.0)
        self.assertEqual(parkingfacility_profile.name, 'Test Parking Facility')
        self.assertEqual(parkingfacility_profile.address, '123 Main Street, Anytown, CA 12345')
        self.assertEqual(parkingfacility_profile.phone_number, '1-800-555-1212')
        self.assertEqual(parkingfacility_profile.website, 'http://www.testparkingfacility.com/')
        self.assertEqual(parkingfacility_profile.rating, 5.0)


class RoadAssistanceTestCase(TestCase):

    def test_road_assistance_model(self):
        road_assistance = RoadAssistance.objects.create(subscriber=Subscriber.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Subscriber', email='testsubscriber@example.com', phone_number='1-800-555-1212'), provider=Provider.objects.create(user=User.objects.create(username='testuser', email='testuser@example.com', password='testpassword'), name='Test Provider', email='testprovider@example.com', phone_number='1-800-555-1212', address='123 Main Street, Anytown, CA 12345'), description='Test road assistance', status='pending')
        self.assertEqual(road_assistance.subscriber.user.username, 'testuser')
        self.assertEqual(road_assistance.subscriber.user.email, 'testuser@example.com')
        self.assertEqual(road_assistance.subscriber.name, 'Test Subscriber')
        self.assertEqual(road_assistance.subscriber.email, 'testsubscriber@example.com')
        self.assertEqual(road_assistance.subscriber.phone_number, '1-800-555-1212')
        self.assertEqual(road_assistance.provider.user.username, 'testuser')
        self.assertEqual(road_assistance.provider.user.email, 'testuser@example.com')
        self.assertEqual(road_assistance.provider.name, 'Test Provider')
        self.assertEqual(road_assistance.provider.email, 'testprovider@example.com')
        self.assertEqual(road_assistance.provider.phone_number, '1-800-555-1212')
        self.assertEqual(road_assistance.provider.address, '123 Main Street, Anytown, CA 12345')
        self.assertEqual(road_assistance.description, 'Test road assistance')
        self.assertEqual(road_assistance.status, 'pending')