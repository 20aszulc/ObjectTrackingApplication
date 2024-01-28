#creating our server side code. import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse
import cv2
import numpy as np

# JSON which maps photos to ID
geisel_photos = [
 {"id":1, "img_src": "geisel-1.jpg"},
 {"id":2, "img_src": "geisel-2.jpg"},
 {"id":3, "img_src": "geisel-3.jpg"},
 {"id":4, "img_src": "geisel-4.jpg"},
 {"id":5, "img_src": "geisel-5.jpg"},
]


# function to access data
def get_photo(request):
   # post_id retrieves the value that is sent by the client
   # the -1 is needed because arrays are 0-indexed
   idx = int(request.matchdict['photo_id'])-1
   # we return the value at the given index from geisel_photos
   return geisel_photos[idx]

def get_price(request):
   # post_id retrieves the value that is sent by the client
   # the -1 is needed because arrays are 0-indexed
   idx = int(request.matchdict['photo_id'])-1
   img1 = cv2.imread("./public/"+geisel_photos[idx]["img_src"])
   img2 = cv2.Canny(img1, 60, 200)
   (width_img2, height) = img2.shape
   mean_img2 = np.mean(img2)
   median_img2 = np.median(img2)
   std_img2 = np.std(img2)
   price_float = mean_img2 + (median_img2 * std_img2) + width_img2
   price = int(price_float)
   print(price)
   return price

def index_page(request):
   return FileResponse('C:/Users/amber/PycharmProjects/ece140/tutorial5/index.html')


# Main entrypoint
if __name__ == '__main__':
    with Configurator() as config:
        # Create a route called home
        config.add_route('home', '/')
        # Bind the view (defined by index_page) to the route named ‘home’
        config.add_view(index_page, route_name='home')
        # Create a route that handles server HTTP requests at: /photos/photo_id
        config.add_route('photos', '/photos/{photo_id}')
        # Binds the function get_photo to the photos route and returns JSON
        # Note: This is a REST route because we are returning a RESOURCE!
        config.add_view(get_photo, route_name='photos', renderer='json')
        config.add_route('price', '/price/{photo_id}')
        priceMe = config.add_view(get_price, route_name='price', renderer='json')
        # Add a static view
        # This command maps the folder “./public” to the URL “/”
        # So when a user requests geisel-1.jpg as img_src, the server knows to look
        # for it in: “public/geisel-1.jpg”
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        # Create an app with the configuration specified above
        app = config.make_wsgi_app()
    print("Server started on port 6543")
    server = make_server('0.0.0.0', 6544, app)  # Start the application on port 6543
    server.serve_forever()
