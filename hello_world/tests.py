from django.test import TestCase, Client

# Create your tests here.

class AppTest(TestCase):
    
    def test_check_availability(self):
        '''
        Check if app is accesible
        '''

        # arrange
        client = Client()
        
        # act
        response = client.get('/hello')
    
        # assert
        self.assertEquals(200, response.status_code)
        
    def test_hello_world_view(self):
        '''
        Check if app view required content
        '''
        
        # arrange
        client = Client()
        
        # act
        response = client.get('/hello')
        
        # assert
        self.assertIn('Hello World!', response.content)